#https://www.acmicpc.net/problem/11725

import sys

sys.setrecursionlimit(int(1e6))
N = int(sys.stdin.readline().rstrip())
tree = [[] for _ in range(N+1)]
parents = [-1]*(N+1)

for n in range(N-1):
    n1, n2 = map(int,sys.stdin.readline().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

def dfs(start):
    for n in tree[start]:
        if parents[n] == -1:
            parents[n] = start
            dfs(n)

dfs(1)
for p in parents[2:]:
    print(p)
