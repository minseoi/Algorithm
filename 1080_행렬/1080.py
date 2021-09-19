#https://www.acmicpc.net/problem/1080

from sys import stdin

R, C = map(int,stdin.readline().split())
matrixA = [list(map(int,list(stdin.readline().rstrip()))) for r in range(R)]
matrixB = [list(map(int,list(stdin.readline().rstrip()))) for r in range(R)]
count = 0

def isEqual():
    for r in range(R):
        for c in range(C):
            if matrixA[r][c] != matrixB[r][c]:
                return False
    return True

def Reverse3x3(R,C):
    for r in range(R,R+3):
        for c in range(C,C+3):
            matrixA[r][c] = 0 if matrixA[r][c] == 1 else 1

for r in range(R-2):
    for c in range(C-2):
        if matrixA[r][c] != matrixB[r][c]:
            Reverse3x3(r,c)
            count+=1

if isEqual():
    print(count)
else:
    print(-1)