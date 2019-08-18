#include <iostream>
#include <string>
using namespace std;

int main() {
	int t;
	cin >> t;
	cin.ignore();
	for (int i=0;i<t;i++){
		string str;
		getline(cin,str);
		size_t D_idx = str.find("D");
		if(D_idx == string::npos){
			D_idx = str.length();
		}
		cout << D_idx << endl;
	}
	return 0;
}
