#https://www.acmicpc.net/problem/7562

from sys import stdin
from collections import deque

def bfs(start, end, _map):
    dx = (1,2,2,1,-1,-2,-2,-1)
    dy = (-2,-1,1,2,2,1,-1,-2)

    startY, startX = start
    endY, endX = end
    queue = deque()
    queue.append([startY,startX])
    _map[startY][startX] = 1

    while queue:
        ny, nx = queue.popleft()
        if ny ==endY and nx == endX: return _map[endY][endX] -1
        for i in range(8):
            nextY = ny + dy[i]
            nextX = nx + dx[i]
            if 0<= nextX < I and 0<= nextY < I:
                if _map[nextY][nextX] == 0:
                    queue.append([nextY,nextX])
                    _map[nextY][nextX] = _map[ny][nx] + 1
    


T = int(stdin.readline().rstrip())
for t in range(T):
    I = int(stdin.readline().rstrip())
    start = list(map(int,stdin.readline().split()))
    end = list(map(int,stdin.readline().split()))
    Map = [[0] * I for _ in range(I)]
    print(bfs(start,end,Map))