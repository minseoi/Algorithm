#https://www.acmicpc.net/problem/2583

from sys import stdin
from collections import deque

M, N, K = map(int,stdin.readline().split())
Map = [[0] * M for _ in range(N)]
areaList = []

for k in range(K):
    x1, y1, x2, y2 = map(int,stdin.readline().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            Map[x][y] = 1

def bfs(x,y):
    if Map[x][y] == 1: return False
    dx = (0,1,0,-1)
    dy = (1,0,-1,0)
    queue = deque([(x,y)])
    count = 1
    Map[x][y] = 1
    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            nextX = nx + dx[i]
            nextY = ny + dy[i]
            if 0<= nextX < N and 0<= nextY < M:
                if Map[nextX][nextY] != 1:
                    queue.append((nextX,nextY))
                    Map[nextX][nextY] = 1
                    count += 1
    global areaList
    areaList.append(count)
    return True

numOfArea = 0
for y in range(M):
    for x in range(N):
        if bfs(x,y):
            numOfArea += 1
print(numOfArea)
areaList.sort()
for a in areaList:
    print(a, end=' ')