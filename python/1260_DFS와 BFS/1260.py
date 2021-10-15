#https://www.acmicpc.net/problem/1260

from collections import deque

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v= queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(graph,v,visited):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

N, M, V = map(int,input().split())
graph = [[] for _ in range(N+1)]

#입력받은 값을 graph리스트에 넣는다.
for _ in range(M):
    i, v = map(int,input().split())
    if v not in graph[i]:
        graph[i].append(v)
    if i not in graph[v]:
        graph[v].append(i)    

#정점번호가 작은 것을 먼저 방문하기 위해 정렬
for v in graph:
    v.sort()

visited = [False]*(N+1)
dfs(graph,V,visited)
print()
visited = [False]*(N+1)
bfs(graph,V,visited)