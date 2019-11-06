#include <bits/stdc++.h>
using namespace std;

int main(){
	char board[8][8];
	for (int i = 0; i < 8; ++i)
	{
		cin >> board[i];
	}
	string program;
	cin >> program;

	bool we_got_the_diamond = false;
	pair<int, int> turtle_pos (0, 0);
	// directions: top, right, bottom, left
	pair<int, int> directions[] = {make_pair(0,1), make_pair(1,0), make_pair(0,-1), make_pair(-1,0)};
	int facing_direction_idx = 1;
	for (int i = 0; i < program.size(); ++i)
	{
		if(program[i]=='F'){
			turtle_pos.first = turtle_pos.first+directions[facing_direction_idx].first;
			turtle_pos.second = turtle_pos.second+directions[facing_direction_idx].second;
			if (board[turtle_pos.first][turtle_pos.second]=='D')
			{
				 we_got_the_diamond = true;
				 break;
			}
			else if(board[turtle_pos.first][turtle_pos.second]=='C' or board[turtle_pos.first][turtle_pos.second]=='I' or turtle_pos.first==0 or turtle_pos.first==7 or turtle_pos.second==0 or turtle_pos.second==7){
				break;
			}
		}
		else if (program[i]=='R'){
			facing_direction_idx = (facing_direction_idx+1)%4;
		}
		else if (program[i]=='L'){
			facing_direction_idx = (facing_direction_idx-1)%4;
		}
		else{
			pair<int, int> lasered_pos (turtle_pos.first+directions[facing_direction_idx].first, turtle_pos.second+directions[facing_direction_idx].second);
			if(board[lasered_pos.first][lasered_pos.second]!='I'){
				break;
			}
			else{
				board[lasered_pos.first][lasered_pos.second] = '.';
			}
		}
	}
	if(we_got_the_diamond){
		cout << "Diamond!";
	}
	else
	{
		cout << "Bug!";
	}
}