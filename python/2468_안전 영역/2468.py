#https://www.acmicpc.net/problem/2468

import sys
import copy
sys.setrecursionlimit(int(1e5))

VISITED = 999
N = int(input())
Map = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

dx = (0,1,0,-1)
dy = (-1,0,1,0)
def dfs(graph, x, y, amountOfRain):
    if graph[y][x] <= amountOfRain or graph[y][x] == VISITED: return False
    graph[y][x] = VISITED
    for i in range(4):
        nextX = x + dx[i]
        nextY = y + dy[i]
        if 0<=nextX<N and 0<=nextY<N:
            if graph[nextY][nextX] > amountOfRain:
                dfs(graph,nextX,nextY,amountOfRain)
    return True

minHeight = 101
maxHeight = 0
for y in range(N):
    for x in range(N):
        minHeight = min(minHeight,Map[y][x])
        maxHeight = max(maxHeight,Map[y][x])
maxAreaCount = 0
for i in range(minHeight-1,maxHeight):
    _map = copy.deepcopy(Map)
    areaCount = 0
    for y in range(N):
        for x in range(N):
            if _map[y][x] != VISITED:
                if dfs(_map,x,y,i):
                    areaCount += 1
    maxAreaCount = max(maxAreaCount,areaCount)

print(maxAreaCount)