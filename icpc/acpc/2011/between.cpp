#include <bits/stdc++.h>
using namespace std;


int main(){
	ifstream cin("between.in");

	int t;
	cin >> t;

	for (int i = 0; i < t; ++i)
	{
		int n;
		cin >> n;
		int mount1[n];
		for (int j = 0; j < n; ++j)
		{
			cin >> mount1[j];
		}

		int m;
		cin >> m;
		int mount2[m];
		for (int j = 0; j < m; ++j)
		{
			cin >> mount2[j];
		}

		int result = 1000000;
		for (int j1 = 0; j1 < n; ++j1)
		{
		 	for (int j2 = 0; j2 < m; ++j2)
		 	{
		 		result = min(result, abs(mount1[j1]-mount2[j2]));
		 	}
		}

		cout << result << "\n";
	}
}
