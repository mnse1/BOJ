import sys
from collections import deque
input = sys.stdin.readline

def op(M):
    global mn, mx
    if operator[0] == operator[1] == operator[2] == operator[3] == 0:
        mx = max(mx, M)
        mn = min(mn, M)
        return
      
    if operator[0] > 0:
        operator[0] -= 1
        n = num.popleft()
        op(M + n)
        operator[0] += 1
        num.appendleft(n)
    if operator[1] > 0:
        operator[1] -= 1
        n = num.popleft()
        op(M - n)
        operator[1] += 1
        num.appendleft(n)
    if operator[2] > 0:
        operator[2] -= 1
        n = num.popleft()
        op(M * n)
        operator[2] += 1
        num.appendleft(n)
    if operator[3] > 0:
        operator[3] -= 1
        n = num.popleft()
        op(int(M/n))
        operator[3] += 1
        num.appendleft(n)
                    
N = int(input())
num = deque(map(int, input().split()))
operator = list(map(int, input().split())) # + - x /

mx = -1000000001
mn = 1000000001

op(num.popleft())
print(mx)
print(mn)