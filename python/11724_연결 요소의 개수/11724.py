#https://www.acmicpc.net/problem/11724

import sys

sys.setrecursionlimit(int(1e8))
N, M = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
for m in range(M):
    n1, n2 = map(int,sys.stdin.readline().split())
    graph[n2].append(n1)
    graph[n1].append(n2)
visited = [False] * (N+1)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

count = 0
for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        count += 1
print(count)