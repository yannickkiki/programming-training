/*
 * ICPC Greater NY Regional, Nov 18, 2018
 * Pinemi puzzles solution by Fred Pickel, C-Scape Consulting Corp
 */
#include <stdio.h>
#include <ctype.h>
#include <math.h>

typedef unsigned char BYTE;
int inPuzzle[10][10];
typedef struct _pinemi_
{
	BYTE nnbrs[10][10];		// for non-stroke boxes number of stroke box nbrs with < 3 strokes
	BYTE remCnt[10][10];	// for stroke boxes, current strokes, for non-stroke, count not yet used
	BYTE remStrokes[10][10];	// for stroke boxes, number of strokes we can still put in the box
	BYTE needStrokes[10][10];	// for stroke boxes, total strokes needed by nbrs at thsi level
	int rowcnt[10];			// number of strokes in each row
	int colcnt[10];			// number of strokes in each col
	int rowbox[10];			// number of stroke boxes in row with rem strokes
	int colbox[10];			// number of stroke boxes in col with rem strokes
} PINEMI, *PPINEMI;

int Validate(PPINEMI pp);

PINEMI soln[100];

// if pp->remStrokes[i][j] > 0, set to zero and check if any non-stroke nbrs have no way to get their count
int ClearStrokes(PPINEMI pp, int i, int j)
{
	int i1, j1;
	if(pp->remStrokes[i][j] == 0) {
		return 0;
	}
	pp->remStrokes[i][j] = 0;
	pp->rowbox[i]--;
	pp->colbox[j]--;
	if((pp->rowbox[i] == 0) && (pp->rowcnt[i] < 10)) {
		return -11;
	}
	if((pp->colbox[j] == 0) && (pp->colcnt[j] < 10)) {
		return -12;
	}
	for(i1 = i-1; i1 <= i+1; i1++) {
		if((i1 < 0) || (i1 > 9)) {
			continue;
		}
		for(j1 = j-1; j1 <= j+1; j1++) {
			if((j1 < 0) || (j1 > 9)) {
				continue;
			}
			if(inPuzzle[i1][j1] > 0) {
				pp->nnbrs[i1][j1]--;
				if((pp->remCnt[i1][j1] > 0) && (pp->nnbrs[i1][j1] == 0)) {
					return -10;
				}
			}
		}
	}
	return 0;
}

// if non-stroke and pp->remCnt < 3, chekc neighboring stroke boxes to be sure remSStrokes <= remCnt
int ChkStrokeNbrs(PPINEMI pp, int i, int j)
{
	int i1, j1, rem, ret;
	if((inPuzzle[i][j] < 0) || ((rem = pp->remCnt[i][j]) >= 3)) {
		return 0;
	}
	for(i1 = i-1; i1 <= i+1; i1++) {
		if((i1 < 0) || (i1 > 9)) {
			continue;
		}
		for(j1 = j-1; j1 <= j+1; j1++) {
			if((j1 < 0) || (j1 > 9)) {
				continue;
			}
			if((inPuzzle[i1][j1] < 0) && (pp->remStrokes[i1][j1] > rem)) {
				if(rem == 0) {
					if((ret = ClearStrokes(pp, i1, j1)) != 0) {
						return ret;
					}
				} else {
					pp->remStrokes[i1][j1] = rem;
				}
			}
		}
	}

	return 0;
}

// add a stroke at i, j for soln in pp, return < 0 if this would cause soln failure
int AddStroke(PPINEMI pp, int i, int j)
{
	int i1, j1, ret;
	if(inPuzzle[i][j] > 0) {
		return -1;
	}
	if(pp->rowcnt[i] >= 10) {
		return -2;
	}
	if(pp->colcnt[j] >= 10) {
		return -3;
	}
	if(pp->remStrokes[i][j] == 0) {
		return -4;
	}
	pp->remStrokes[i][j]--;
	pp->remCnt[i][j]++;
	pp->rowcnt[i]++;
	pp->colcnt[j]++;
	if((pp->rowcnt[i] >= 10) || (pp->colcnt[j] >= 10)) {	// row or col full cannot ad more here
		pp->remStrokes[i][j] = 0;
	}
	if(pp->remStrokes[i][j] == 0) {
		pp->rowbox[i]--;
		pp->colbox[j]--;
	}
	for(i1 = i-1; i1 <= i+1; i1++) {
		if((i1 < 0) || (i1 > 9)) {
			continue;
		}
		for(j1 = j-1; j1 <= j+1; j1++) {
			if((j1 < 0) || (j1 > 9)) {
				continue;
			}
			if(inPuzzle[i1][j1] > 0) {
				if(pp->remCnt[i1][j1] == 0) {
					return -5;
				}
				pp->remCnt[i1][j1]--;
				if(pp->remCnt[i1][j1] < 3) {
					if((ret = ChkStrokeNbrs(pp, i1, j1)) != 0) {
						return ret;
					}
				}
				if(pp->remStrokes[i][j] == 0) {
					pp->nnbrs[i1][j1]--;
				}
				if((pp->remCnt[i1][j1] > 0) && (pp->nnbrs[i1][j1] == 0)) {
					return -6;
				}
			}
		}
	}
	// if row or col cnt = 10, go thru othe stroke boxes in row and set their remcnts to 0
	if(pp->rowcnt[i] == 10) {
		for(j1 = 0; j1 < 10 ; j1++) {
			if(pp->remStrokes[i][j1] > 0) {
				if((ret = ClearStrokes(pp, i,  j1)) != 0) {
					return ret;
				}
			}
		}
	}
	if(pp->colcnt[j] == 10) {
		for(i1 = 0; i1 < 10 ; i1++) {
			if(pp->remStrokes[i1][j] > 0) {
				if((ret = ClearStrokes(pp, i1,  j)) != 0) {
					return ret;
				}
			}
		}
	}
	return 0;
}

// scan inPuzzle and set each stroke location intially to 1
// set nbrs and rem cnt in soln[0]
int PinemiInit()
{
	PPINEMI pp = &(soln[0]);
	int i, j, i1, j1, ret, rsum, csum[10];
	for(i = 0; i < 10 ; i++) {
		pp->rowcnt[i] = pp->colcnt[i] = pp->rowbox[i] = pp->colbox[i] = csum[i] = 0;
		for(j = 0; j < 10; j++) {
			pp->nnbrs[i][j] = 0;
			if(inPuzzle[i][j] > 0) {
				pp->remCnt[i][j] = inPuzzle[i][j];
			} else {
				pp->remCnt[i][j] = 0;
			}
		}
	}
	for(i = 0; i < 10 ; i++) {
		rsum = 0;
		for(j = 0; j < 10 ; j++) {
			if(inPuzzle[i][j] < 0) {	// stroke box
				pp->rowbox[i]++;
				pp->colbox[j]++;
				pp->remStrokes[i][j] = 3;
				for(i1 = i-1; i1 <= i+1; i1++) {
					if((i1 < 0) || (i1 > 9)) {
						continue;
					}
					for(j1 = j-1; j1 <= j+1; j1++) {
						if((j1 < 0) || (j1 > 9)) {
							continue;
						}
						if(inPuzzle[i1][j1] > 0) {
							if(pp->remCnt[i1][j1] < pp->remStrokes[i][j]) {
								pp->remStrokes[i][j] = pp->remCnt[i1][j1];
							}
							pp->nnbrs[i1][j1]++;
						}
					}
				}
			} else {
				pp->remStrokes[i][j] = 0;
			}
			rsum += pp->remStrokes[i][j];
			csum[j] += pp->remStrokes[i][j];
		}
		if(rsum < 10) {
			printf("row %d sum avail %d < 10\n", i+1, rsum);
			return -20;
		}
	}
	for(j = 0; j < 10 ; j++) {
		if(csum[j] < 10) {
			printf("col %d sum avail %d < 10\n", j+1, csum[j]);
			return -21;
		}
	}
	// now set each stroke box to 1;
	for(i = 0; i < 10 ; i++) {
		for(j = 0; j < 10 ; j++) {
			if(inPuzzle[i][j] < 0) {	// stroke box
				if((ret = AddStroke(pp, i, j)) != 0) {
					printf("AddStroke ret %d at %d, %d\n", ret, i, j);
					return ret;
				}
			}
		}
	}
	return 0;
}


char *solnStr[4] = {"   ", "  |", " ||", "|||"};
void PrintSoln1(int probNum, PPINEMI pp)
{
	int i, j;
	printf("%d\n", probNum);
	for(i = 0; i < 10 ; i++) {
		for(j = 0; j < 10 ; j++) {
			if(inPuzzle[i][j] > 0) {
				printf(" %3d", inPuzzle[i][j]);
			} else {
				printf(" %s", solnStr[pp->remCnt[i][j]]);
			}
		}
		printf("\n");
	}
}

void PrintSoln(int probNum, PPINEMI pp)
{
	int i, j;
	printf("%d\n", probNum);
	for(i = 0; i < 10 ; i++) {
		for(j = 0; j < 10 ; j++) {
			if(inPuzzle[i][j] > 0) {
				printf(" %2d", inPuzzle[i][j]);
			} else {
				printf(" %2d", pp->remCnt[i][j]);
			}
		}
		printf("\n");
	}
}

int ChkSoln(PPINEMI pp)
{
	int i, j;
	for(i = 0; i < 10 ; i++) {
		if(pp->rowcnt[i] < 10) {
			return -50;
		}
		if(pp->colcnt[i] < 10) {
			return -51;
		}
		for(j = 0; j < 10 ; j++) {
			if((inPuzzle[i][j] > 0) && (pp->remCnt[i][j] > 0)) {
				return -52;
			}
		}
	}
	return 0;
}


int Solve(int probNum, int level, int inew, int jnew)
{
	PPINEMI pp, ppn;
	int i, j, cfull, rfull, ret;
	int i1, j1;
	int minbox, minboxcol, minboxrow, minboxcnt;
	pp = &(soln[level]);
	ppn = &soln[level+1];
	*ppn = *pp;
	// if newi, newj >= 0 try to AddStoke at inew, jnew
	if((inew >= 0) && (jnew >= 0)) {
		if((ret = AddStroke(ppn, inew, jnew)) != 0) {
			return ret;
		}
	}
	// scan for row or col with only one active box and strokes still needed
	cfull = rfull = 0;
	for(i = 0; i < 10 ; i++) {
		if(ppn->rowcnt[i] == 10) rfull++;
		else if(ppn->rowbox[i] == 1) {
			for(j = 0; j < 10; j++) {
				if(ppn->remStrokes[i][j] > 0) {
					while((ppn->rowcnt[i] < 10) && (ppn->remStrokes[i][j] > 0)) {
						if((ret = AddStroke(ppn, i, j)) != 0) {
							return ret;
						}
					}
					if(ppn->rowcnt[i] < 10) {
						return -30;
					} else {
						rfull++;
					}
					break;
				}
			}
		}
		if(ppn->colcnt[i] == 10) cfull++;
		else if(ppn->colbox[i] == 1) {
			for(j = 0; j < 10; j++) {
				if(ppn->remStrokes[j][i] > 0) {
					while((ppn->colcnt[i] < 10) && (ppn->remStrokes[j][i] > 0)) {
						if((ret = AddStroke(ppn, j, i)) != 0) {
							return ret;
						}
					}
					if(ppn->colcnt[i] < 10) {
						return -31;
					} else {
						cfull++;
					}
					break;
				}
			}
		}
	}
	if((rfull == 10) && (cfull == 10) && (ChkSoln(ppn) == 0)) {
		PrintSoln(probNum, ppn);
		return 0;
	}
	// look for non-stroke boxes with only one neighbor
	for(i = 0; i < 10 ; i++) {
		for(j = 0; j < 10 ; j++) {
			if((inPuzzle[i][j] > 0) && (ppn->remCnt[i][j] > 0) && (ppn->nnbrs[i][j] == 1)) {
				for(i1 = i-1; i1 <= i+1; i1++) {
					if((i1 < 0) || (i1 > 9)) {
						continue;
					}
					for(j1 = j-1; j1 <= j+1; j1++) {
						if((j1 < 0) || (j1 > 9)) {
							continue;
						}
						if((inPuzzle[i1][j1] < 0) && (ppn->remStrokes[i1][j1] > 0)){
							while((ppn->remCnt[i][j] > 0) && (ppn->remStrokes[i1][j1] > 0)){
								if((ret = AddStroke(ppn, i1, j1)) != 0) {
									return ret;
								}
							}
							if(ppn->remCnt[i][j] > 0) {
								return -40;
							}
						}
					}
				}
			}
		}
	}
	if(ChkSoln(ppn) == 0) {
		PrintSoln(probNum, ppn);
		return 0;
	}
	// pick a row or col and try each stroke box in it, prefer one wiht less active boxes
	minbox = 10;
	minboxcnt = 0;
	minboxrow = minboxcol = -1;
	for(i = 0; i < 10 ; i++) {
		if((ppn->rowbox[i] > 0) && ((ppn->rowbox[i] < minbox) ||
			((ppn->rowbox[i] == minbox) && (minboxcnt > ppn->rowcnt[i])))) {
			minbox = ppn->rowbox[i];
			minboxrow = i;
			minboxcnt = ppn->rowcnt[i];
		}
	}
	for(i = 0; i < 10 ; i++) {
		if((ppn->colbox[i] > 0) && ((ppn->colbox[i] < minbox) ||
			((ppn->colbox[i] == minbox) && (minboxcnt > ppn->colcnt[i])))) {
			minbox = ppn->colbox[i];
			minboxcol = i;
			minboxrow = -1;
			minboxcnt = ppn->rowcnt[i];
		}
	}
	if(minboxrow >= 0) {
		for(i = 0; i < 10 ; i++) {
			if(ppn->remStrokes[minboxrow][i] > 0) {
				if(Solve(probNum, level+1, minboxrow, i) == 0) {
					return 0;
				}
			}
		}
	} else {
		for(i = 0; i < 10 ; i++) {
			if(ppn->remStrokes[i][minboxcol] > 0) {
				if(Solve(probNum, level+1, i, minboxcol) == 0) {
					return 0;
				}
			}
		}
	}
	// nothing worked, back up
	return -41;
}

char inbuf[256];
int main()
{
	int nprob, curprob, index, ret;
	int i;
	if(fgets(&(inbuf[0]), 255, stdin) == NULL)
	{
		fprintf(stderr, "Read failed on problem count\n");
		return -1;
	}
	if(sscanf(&(inbuf[0]), "%d", &nprob) != 1)
	{
		fprintf(stderr, "Scan failed on problem count\n");
		return -2;
	}
	for(curprob = 1; curprob <= nprob ; curprob++)
	{
		if(fgets(&(inbuf[0]), 255, stdin) == NULL)
		{
			fprintf(stderr, "Read failed on problem %d header\n", curprob);
			return -3;
		}
		if(sscanf(&(inbuf[0]), "%d", &index) != 1) {
			fprintf(stderr, "scan failed on problem %d header\n", curprob);
			return -4;
		}
		if(index != curprob) {
			fprintf(stderr, "problem index %d not = expected problem %d\n",
				index, curprob);
			return -5;
		}
		for(i = 0; i < 10 ; i++) {
			if(fgets(&(inbuf[0]), 255, stdin) == NULL)
			{
				fprintf(stderr, "Read failed on problem %d row %d\n", curprob, i+1);
				return -6;
			}
			if(sscanf(&(inbuf[0]), "%d %d %d %d %d %d %d %d %d %d",
				&inPuzzle[i][0], &inPuzzle[i][1], &inPuzzle[i][2], &inPuzzle[i][3], &inPuzzle[i][4], 
				&inPuzzle[i][5], &inPuzzle[i][6], &inPuzzle[i][7], &inPuzzle[i][8], &inPuzzle[i][9]) != 10) {
				fprintf(stderr, "scan failed on problem %d row %d\n", curprob, i+1);
				return -7;
			}
		}
		if((ret = PinemiInit()) != 0) {
			return ret;
		}
		if((ret = Solve(curprob, 0, -1, -1)) != 0) {
			return ret;
		}
	}
	return 0;
}
