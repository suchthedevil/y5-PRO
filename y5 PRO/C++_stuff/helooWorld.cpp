#include <iostream>
#include <chrono>
using namespace std;

int main() {
    auto start = chrono::high_resolution_clock::now();
    int p = 15;
    int c = 10;
    int mySum = c+p;
    cout << mySum; cout << "\n";
    cout << "Hello World!";         //Anything after the double-slash until the end of the line is ignored by the compiler
    auto finish = chrono::high_resolution_clock::now();
    auto microseconds = chrono::duration_cast<chrono::microseconds>(finish-start);
    cout << "\n" << microseconds.count()<< "microsec";
    return 0;
}
