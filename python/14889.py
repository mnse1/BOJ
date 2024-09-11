import sys
from collections import deque
input = sys.stdin.readline

def get_min_dif():
    ss = sl = 0
    for i in range(len(start)):
        for j in range(i, len(start)):
            ss += S[start[i]-1][start[j]-1]
            ss += S[start[j]-1][start[i]-1]
    for i in range(len(link)):
        for j in range(i, len(link)):
            sl += S[link[i]-1][link[j]-1]
            sl += S[link[j]-1][link[i]-1]
    
    return abs(ss-sl)

def divide():
    global difference
    if len(start) == len(link) == N//2:
        difference = min(difference, get_min_dif())
        return
    
    if len(start) < N//2:
        a = people.popleft()
        start.append(a)
        divide()
        start.pop()
        people.appendleft(a)
    if len(link) < N//2:
        a = people.popleft()
        link.append(a)
        divide()
        link.pop()
        people.appendleft(a)

N = int(input())  #always even
people = deque(int(i)+1 for i in range(N))
S = [list(map(int, input().split())) for _ in range(N)]
start = []
link = []
difference = 99999999

divide()
print(difference)