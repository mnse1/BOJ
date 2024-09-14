import sys
input = sys.stdin.readline

def dp(N): 
    if N==1:
        return tile[1]
    if N==2:
        return tile[2]
    for i in range(3, N+1):
        tile[i] = (tile[i-1] + tile[i-2]) % 15746
    return tile[N]
    
N = int(input())
tile = [0] * (N+2)
tile[1] = 1
tile[2] = 2

print(dp(N))
