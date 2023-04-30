#https://www.acmicpc.net/problem/4963

import sys

sys.setrecursionlimit(int(1e8))
#방향: 위에서부터 시계방향으로 8방향
dw = (0,1,1,1,0,-1,-1,-1)
dh = (-1,-1,0,1,1,1,0,-1)

def dfs(graph, w,h):
    graph[h][w] = 0 #방문 체크
    for i in range(8): #방향
        new_w = w + dw[i]
        new_h = h + dh[i]
        if (0<=new_w<W and 0<=new_h<H):
            if graph[new_h][new_w] == 1:
                dfs(graph,new_w,new_h)

while True:
    W,H = map(int,sys.stdin.readline().split())
    count = 0
    if W==0 and H==0:
        break
    Map = [list(map(int,sys.stdin.readline().split())) for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if Map[h][w] == 1:
                dfs(Map,w,h)
                count += 1
    print(count)