#https://www.acmicpc.net/problem/2606

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
count = 0
for m in range(M):
    n1, n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

def dfs(graph, v, visited):
    global count
    count+=1
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

dfs(graph,1,visited)
print(count-1)