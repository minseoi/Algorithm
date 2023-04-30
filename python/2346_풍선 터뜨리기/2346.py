#https://www.acmicpc.net/problem/2346

from sys import stdin

N = int(stdin.readline().rstrip())
balloons = list(map(int,stdin.readline().split()))
visited = [False]*N
result = []

pos = 0
for i in range(N):
    result.append(pos+1)
    visited[pos] = True
    if False not in visited:
        break
    target = balloons[pos]
    count = 0
    delta = 1 if target>0 else -1
    while count < abs(target):
        pos += delta
        if pos < 0: pos = N-1
        if pos >= N: pos = 0
        if visited[pos] == False:
            count+= 1
print(*result)