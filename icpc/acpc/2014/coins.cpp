#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long int ll;

int main(){
	int t, s, n;
	ifstream cin("coins.in");
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		cin >> s >> n;
		int value[n], number[n];
		for (int ci = 0; ci < n; ++ci)
		{
			cin >> value[ci] >> number[ci];
			// cout << value[ci] << " " << number[ci] << "\n";
		}

		ll result = 0;
		for (int r = 1; r <= s; ++r)
		{
			if(s%r==0){
				int sub_s = s/r;
				// cout << sub_s << " ";
				ll count[sub_s+1] = {1};
				for (int ci = 0; ci < n; ++ci)
				{
					// cout << "V" << value[ci] << " ";
					if(number[ci]>=r){
						for (int v = sub_s; v >= value[ci]; --v)
						{
							count[v] += count[v-value[ci]];
						}
					}
				}
				// cout << "C" << count[sub_s] << " ";
				result += count[sub_s];
			}
		}
		cout << "Case " << i+1 << ": " << result << "\n";
	}
}
