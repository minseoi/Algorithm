#https://www.acmicpc.net/problem/2644

from sys import stdin
from collections import deque

n = int(stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
start, end = map(int,stdin.readline().split())
m = int(stdin.readline().rstrip())
for _ in range(m):
    x, y = map(int,stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

grade = [-1] * (n+1)
def bfs(start):
    queue = deque([start])
    grade[start] = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if grade[i] == -1:
                queue.append(i)
                grade[i] = grade[v] + 1
                if i == end:
                    return

bfs(start)
print(grade[end])