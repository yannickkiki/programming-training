#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iterator>
#include <iostream>

using namespace std;

void join(vector<int> &v, string delimiter){

}
int main()
{
    vector<int> v = {5,4,2,3,6};
//    vector<int> vec(v.cbegin(), v.cbegin()+2);
//    for (int e : vec) {
//        cout << " " << e;
//    }
//    sort(v.begin(), v.end());
//
//    do {
//        for (int e : v) {
//            cout << " " << e;
//        }
//        cout << endl;
//    } while (next_permutation(v.begin(), v.end()));

    ostringstream vts;
    copy(v.begin(), v.end()-1, ostream_iterator<int>(vts, " "));
    // Now add the last element with no delimiter
    vts << v.back();
    string result = vts.str();
    cout << result << endl;
}
