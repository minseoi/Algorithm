#https://www.acmicpc.net/problem/1987

import sys

sys.setrecursionlimit(100000)

R, C = map(int,sys.stdin.readline().split())
Map = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
visited = set(Map[0][0])

dx = (0,1,0,-1)
dy = (-1,0,1,0)
def dfs(x, y, count):
    global result
    result = max(result,count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < C and 0<= ny < R:
            if Map[ny][nx] not in visited:
                visited.add(Map[ny][nx])
                dfs(nx, ny, count+1)
                visited.remove(Map[ny][nx])

result = 0
dfs(0,0,1)
print(result)