#include <iostream>
using namespace std;

int n, board[100][100];

bool jump(int y, int x) {
    if (y >= n || x >= n) return false;
    if (y == n-1 && x== n-1) return true;
    int jumpSize = board[y][x];
    return jump(y + jumpSize, x) || jump(y, x + jumpSize);
}


int main() {
    int cases;
    cin >> cases;
    while(cases--) {
        int lines;
        cin >> lines;
        cin.ignore();
        while (lines--) {
            string line;
            getline(cin, line);
            cout << cases << '/' << lines << '/' << line << endl;
        }
    }
    return 0;
}