#https://www.acmicpc.net/problem/10026

import copy
from collections import deque

def ColorBlind(pic):
    result = copy.deepcopy(pic)
    for y in range(N):
        for x in range(N):
            if result[y][x] == 'G':
                result[y][x] = 'R'
    return result

dx = (0,1,0,-1)
dy = (-1,0,1,0)

def bfs(graph,x,y):
    if graph[y][x] == "": return False
    queue = deque([(y,x)])
    refColor = graph[y][x]
    graph[y][x] = ""
    while queue:
        v = queue.popleft()
        for i in range(4):
            new_y = v[0] + dy[i]
            new_x = v[1] + dx[i]
            if 0<=new_x<N and 0<=new_y<N:
                if graph[new_y][new_x] == refColor:
                    queue.append((new_y,new_x))
                    graph[new_y][new_x] = ""
    return True



N = int(input())
colorPic = [list(input()) for _ in range(N)]
blindPic = ColorBlind(colorPic)

colorCount = 0
blindCount = 0
for y in range(N):
    for x in range(N):
        colorCount += 1 if bfs(colorPic,x,y) else 0
        blindCount += 1 if bfs(blindPic,x,y) else 0

print(colorCount, end=' ')
print(blindCount)