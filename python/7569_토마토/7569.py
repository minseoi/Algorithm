#https://www.acmicpc.net/problem/7569

from sys import stdin

VALID = 1
INVALID = 0
BLANK = -1

dm = [0, 0, +1, 0, -1, 0]
dn = [0, +1, 0, -1, 0, 0]
dh = [-1, 0, 0, 0, 0, +1]

M, N, H = map(int,stdin.readline().split())
Box = [[list(map(int,stdin.readline().split())) for n in range(N)] for h in range(H)]
validTomatoes = []
TotalTomatoes = 0
NumOfValidTomatoes = 0

for h in range(H):
    for n in range(N):
        for m in range(M):
            if Box[h][n][m] == VALID:
                validTomatoes.append([h,n,m])
                NumOfValidTomatoes += 1
            if Box[h][n][m] != BLANK:
                TotalTomatoes += 1

##############################################################################
def BFS(validTomatoes):
    global NumOfValidTomatoes
    Day = 0
    while(True):
        nextValidTomatosCache = []
        while(validTomatoes):
            tomato = validTomatoes.pop()
            _H = tomato[0]
            _N = tomato[1]
            _M = tomato[2]
            for i in range(6):
                next_H = _H+dh[i]
                next_N = _N+dn[i]
                next_M = _M+dm[i]
                if 0 <= next_H < H and 0 <= next_N < N and 0 <= next_M < M:
                    if Box[next_H][next_N][next_M] == INVALID:
                        Box[next_H][next_N][next_M] = VALID
                        nextValidTomatosCache.append([next_H,next_N,next_M])
                        NumOfValidTomatoes += 1
            
        if len(nextValidTomatosCache) != 0:
            validTomatoes = nextValidTomatosCache[:]
            Day+=1
            continue
        else:
            return Day
##############################################################################

if NumOfValidTomatoes == TotalTomatoes:
    print(0)
else:
    day = BFS(validTomatoes)
    if NumOfValidTomatoes == TotalTomatoes:
        print(day)
    else:
        print(-1)