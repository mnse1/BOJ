import copy
import sys
input = sys.stdin.readline

def dfs():
    if len(l) == M:
        print(*l)
        return
    for i in range(N):
        if i+1 not in l:
            l.append(i+1)
            dfs()
            l.pop()

N, M = map(int, input().split())
l = []
dfs()