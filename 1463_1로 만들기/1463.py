#https://www.acmicpc.net/problem/1463

import sys

N = int(sys.stdin.readline())
usedNum = [0] * 1000001

for n in range(2,N+1):
    usedNum[n] = usedNum[n-1]+1
    if n%3 == 0:
        usedNum[n] = min(usedNum[n], usedNum[n//3]+1)
    if n%2 == 0:
        usedNum[n] = min(usedNum[n],usedNum[n//2]+1)

print(usedNum[N])