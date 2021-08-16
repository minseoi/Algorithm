#https://www.acmicpc.net/problem/14502

from sys import stdin
from collections import deque
import copy

N,M = map(int,stdin.readline().split())
Map = [list(map(int,stdin.readline().split())) for _ in range(N)]
maxSafeSpace = 0
dx = (0,1,0,-1)
dy = (-1,0,1,0)

def bfs():
    graph = copy.deepcopy(Map)
    safeSpace = 0
    queue = deque()
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 2:
                queue.append((y,x))
            elif graph[y][x] == 0:
                safeSpace += 1
    count = 0
    while queue:
        vP = queue.popleft()
        for i in range(4):
            new_y = vP[0] + dy[i]
            new_x = vP[1] + dx[i]
            if 0<=new_x<M and 0<=new_y<N: 
                if graph[new_y][new_x] == 0:
                    queue.append((new_y,new_x))
                    graph[new_y][new_x] = 2
                    count += 1
    global maxSafeSpace
    maxSafeSpace = max(maxSafeSpace,safeSpace - count)

def Wall(n,_x,_y):
    if n == 3:
        bfs()
        return
    else:
        for y in range(_y,N):
            for x in range(_x,M):
                if Map[y][x] == 0:
                    Map[y][x] = 1
                    Wall(n+1,x,y)
                    Map[y][x] = 0
            _x = 0

Wall(0,0,0)
print(maxSafeSpace)