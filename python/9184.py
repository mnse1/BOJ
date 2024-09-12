import sys
input = sys.stdin.readline

def w(a, b, c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        return w(20, 20, 20)
    if wlist[a][b][c] != 0:
        return wlist[a][b][c]
    if a<b<c:
        wlist[a][b][c] += w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return wlist[a][b][c]
    wlist[a][b][c] += w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return wlist[a][b][c]

wlist = [[[0] * 21 for _ in range(21)] for _ in range(21)]

while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c,)}')