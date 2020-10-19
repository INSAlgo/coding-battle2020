// Solution by Emma Neiss

#include <iostream>

using namespace std;

int main(int argc, char **argv) {

    int n, p1, p2, p3;
    // read the 4 integers given as nput
    cin >> n >> p1 >> p2 >> p3;

    int res;

    // two ways of solving the problem, choose one below

    // shorter version
    res = min(n, 100)*p1 + min(max(n - 100, 0), 100)*p2 + max(n - 200, 0)*p3;

    // longer version
    if (n <= 100) {
        res = n*p1;
    } else if (n <= 200) {
        res = 100*p1 + (n-100)*p2;
    } else {
        res = 100*p1 + 100*p2 + (n-200)*p3;
    }

    cout << res;

    return 0;
}