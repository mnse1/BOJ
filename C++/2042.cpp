#include <iostream>
#include <algorithm>
using namespace std;

long long int arr[1000001];
long long int sum[1000001];
long long int answer[10001];
int main() {
    long int n;
    int  m, k, idx = 1;
    
    cin >> n >> m >> k;
    for(int i = 1; i <= n; i++) cin >> arr[i];
    for(int i = 1; i <= n; i++) sum[i] = sum[i-1] + arr[i];
    for(int i = 1; i <= m+k; i++) {
        int a;
        long long int b, c;
        cin >> a >> b >> c;
        if (a == 1) {
            int diff = arr[b] - c;
            for(int i = b; i <= n; i++) sum[i] -= diff;
            arr[b] = c;
        }
        else if(a == 2) {
            answer[idx++] =  sum[c]-sum[b-1];
        }
    }
    for(int i = 1; i <= k; i++) cout << answer[i] << "\n";
    
    return 0;
}