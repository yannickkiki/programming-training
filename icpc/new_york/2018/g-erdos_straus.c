/*
 * ICPC Greater NY Regional, Nov 18 2018
 * Solution for Erdos Straus problem by Fred Pickel
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

typedef unsigned long DWORD;
#ifdef WIN32
typedef unsigned __int64 DDWORD;
#else
typedef unsigned long long DDWORD
#endif

#define MAX_N	50000
// a and b >= 0
DDWORD GCDU64(DDWORD a, DDWORD b)
{
	DDWORD r;
	if(a == 0) return b;
	if(b == 0) return a;
	if((a == 1) || (b == 1)) return 1;
	if(a == b) return a;
	r = a % b;
	while(r != 0) {
		a = b;
		b = r;
		r = a % b;
	}
	return b;
}

int Erdos_StraussMin(int n, DDWORD *presult)
{
	DDWORD k, last, first, num, i, j;
	DDWORD denom;
	DDWORD firstj, lastj, rem;
	first = 1 + (n/4);
	last = (3*n)/4;
	for(k = first; k <= last ; k++) {
		denom = n*k;
		num = 4*k - n;	//numerator of difference over denom of n*k
		i = GCDU64(num, denom);
		denom /= i;
		num /= i;
		if(num == 1) {
			presult[0] = k;
			presult[1] = denom + 1;
			presult[2] = denom*(denom + 1);
			return 0;
		}
		firstj = denom/num + 1;
		lastj = (2*denom)/num;
		for(j = firstj; j <= lastj ; j++) {
			rem = j*num - denom;
			if(((j*denom) % rem) == 0) {
				presult[0] = k;
				presult[1] = j;
				presult[2] = (j*denom)/rem;
				return 0;
			}
		}
	}
	return -1;
}

char inbuf[256];

int main()
{
	int nprob, curprob, index, ret, n;
	DDWORD result3[3];
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
		// get prob num and triangle vertices
		if(sscanf(&(inbuf[0]), "%d %d", &index, &n) != 2)
		{
			fprintf(stderr, "scan failed on problem header problem index %d\n",
				curprob);
			return -6;
		}
		if(index != curprob)
		{
			fprintf(stderr, "problem index %d not = expected problem %d\n",
				index, curprob);
			return -7;
		}
		if(n > MAX_N)
		{
			fprintf(stderr, "problem index %d n %d > MAX %d\n",
				index, n, MAX_N);
			return -8;
		}
		if((ret = Erdos_StraussMin(n, result3)) == 0) {
				printf("%d %llu %llu %llu\n", index, result3[0], result3[1], result3[2]);
		} else {
			printf("Min method ret %d\n", ret);
		}
	}
	return 0;
}
