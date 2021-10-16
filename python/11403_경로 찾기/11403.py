#https://www.acmicpc.net/problem/11403

from sys import stdin

N = int(stdin.readline().rstrip())
matrix = [list(map(int,stdin.readline().split())) for _ in range(N)]
graph = [[] for i in range(N)]
for c in range(N):
    for r in range(N):
        if matrix[c][r] != 0:
            graph[c].append(r)

def dfs(start, graph, visited, isRecursion = False):
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i,graph,visited,True)

for c in range(N):
    visited = [False]*N
    dfs(c,graph,visited)
    print(*map(int,visited))