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
        cin >> n;
        for (int x = 0; x < n; x++) {
            for (int y = 0; y < n; y++) {
                cin >> board[y][x];
            }
        }
        cout << (jump(0, 0) ? "YES" : "NO") << endl;
    }
    return 0;
}