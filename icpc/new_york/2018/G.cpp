#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long int ll;


int main(){
	ifstream cin("G.in");

	int t;
	cin >> t;

	for (int i = 0; i < t; ++i)
	{
		int k, n;
		ll a_, b_, c_;
		cin >> k >> n;

		ll a_inf = 1 + (n/4);
		ll a_sup = 3*n/4;

		bool is_found = false;

		for (ll a=a_inf; a<=a_sup; ++a)
		{
			ll b_inf = (a*n)/(4*a-n);
			ll b_sup = 2*b_inf;
			b_inf += 1;
			for (ll b=b_inf; b<=b_sup; ++b)
			{
				ll c_num = a*b*n;
				ll c_den = 4*a*b-a*n-b*n;
				if(c_num%c_den==0){
					a_ = a;
					b_ = b;
					c_ = c_num/c_den;
					is_found = true;
					break;
				}
			}
			if(is_found){
				cout << k << " " << a_ << " " << b_ << " " << c_ << "\n";
				break;
			}
		}
	}
}
