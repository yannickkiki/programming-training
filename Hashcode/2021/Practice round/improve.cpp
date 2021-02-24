#include <iostream>
#include <chrono>

using namespace std;

int main() {
    auto starttime = chrono::high_resolution_clock::now();
    cout << "Diamond!" << endl;
    auto endtime = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed_seconds = endtime - starttime;
    cout << elapsed_seconds.count() << endl;
}
