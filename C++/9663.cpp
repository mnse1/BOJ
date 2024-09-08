#include <iostream>
using namespace std;

int board[15];
int N;
int count = 0;
int cd(int n);
int chess(int n);

int main() {
    
    cin >> N;

    chess(0);
    cout << count << "\n";

    return 0;
}

int cd(int n) {
    for(int i = 0; i < n; i++) {
        if (board[i] == board[n] or abs(board[n]-board[i]) == abs(n-i))
            return 0;
    }
    return 1;
}

int chess(int n) {
    if(n == N) {
        count++;
        return 0;
    }
    for(int i = 0; i < N; i++) {
        board[n] = i;
        if (cd(n)) chess(n+1);
    }
    return 0;
}