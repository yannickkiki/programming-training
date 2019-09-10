#include <bits/stdc++.h>
using namespace std;

int main(){
	string expression;
	cin >> expression;

	vector<pair<int, int>> brackets_positions;
	stack<int> open_brackets_positions;

	for (int idx = 0; idx < expression.size(); ++idx){
		if(expression[idx] == '('){
			open_brackets_positions.push(idx);
		}
		else if(expression[idx] == ')'){
			pair <int,int> couple_of_brackets (open_brackets_positions.top(), idx);
			brackets_positions.push_back(couple_of_brackets);
			open_brackets_positions.pop();
		}
	}

	int number_of_possibilities = 1 << brackets_positions.size();
	vector<string> result;
	for (int disposition = 1; disposition < number_of_possibilities; ++disposition){
		vector<bool> print(expression.size(), true);
		string expression_obtained;
		for (int bracket_pair_idx=0; bracket_pair_idx<brackets_positions.size(); ++bracket_pair_idx){
			if(disposition & (1<<bracket_pair_idx)){
				print[brackets_positions[bracket_pair_idx].first] = false;
				print[brackets_positions[bracket_pair_idx].second] = false;
			}
		}

		for (int i = 0; i < expression.size(); ++i){
			if(print[i]){
				expression_obtained+=expression[i];
			}
		}

		result.push_back(expression_obtained);
	}

	sort(result.begin(), result.end()); 
	result.erase(unique(result.begin(), result.end()), result.end());
	for(auto exp : result) {
        cout << exp << endl;
    }
}
