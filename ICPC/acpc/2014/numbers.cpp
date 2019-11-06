#include <bits/stdc++.h>
using namespace std;

unsigned long long int gcd(unsigned long long int a, unsigned long long int b){
	if(b==0){
		return a;
	}
	else{
		return gcd(b, a%b);
	}
}

int main(){
	int suit_size = 72;
	unsigned long long int suit[suit_size];
	suit[0] = 0;
	suit[1] = 1;
	for (int i = 2; i < suit_size; ++i)
	{
		suit[i] = suit[i-1]+suit[i-2];
	}

	ifstream file("numbers.in");
	int t;
	file >> t;
	int x,n,y,m;
	for (int i = 0; i < t; ++i)
	{
		file >> x >> n >> y >> m;
		unsigned long long int a = suit[n+1]*x+y;
		unsigned long long int b = suit[n]*x;
		// cout << a << " " << b << " " << suit[71];
		cout << "Case " << i+1 << ": " << gcd(a, b) << "\n";
	}
}