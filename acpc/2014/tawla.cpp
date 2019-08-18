#include <bits/stdc++.h>
using namespace std;

unordered_map<int, string> dice_names;

unordered_map<int, string> dice_pair_names;


string tawla_name(int d1, int d2){
	if(d1+d2==11){
		return "Sheesh Beesh";
	}
	else if(d1==d2){
		return dice_pair_names[d1];
	}
	else if(d1>d2){
		return dice_names[d1]+" "+dice_names[d2];
	}
	else{
		return dice_names[d2]+" "+dice_names[d1];
	}
}

int main(){
	string line;
	int n, d1, d2;

	dice_names[1]="Yakk";
	dice_names[2]="Doh";
	dice_names[3]="Seh";
	dice_names[4]="Ghar";
	dice_names[5]="Bang";
	dice_names[6]="Sheesh";

	dice_pair_names[1]="Habb Yakk";
	dice_pair_names[2]="Dobara";
	dice_pair_names[3]="Dousa";
	dice_pair_names[4]="Dorgy";
	dice_pair_names[5]="Dabash";
	dice_pair_names[6]="Dosh";

	ifstream file("tawla.in");
	file >> n;
	for (int i = 0; i < n; ++i)
	{
		file >> d1 >> d2;
		string name = tawla_name(d1, d2);
		cout << "Case " << i+1 << ": " << name << "\n";
	}
}
