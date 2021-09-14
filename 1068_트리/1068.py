#https://www.acmicpc.net/problem/1068

from sys import stdin

N = int(stdin.readline().rstrip())
Tree = [[] for _ in range(N)] 
rootNodes = set(i for i in range(N))

n = 0
for i in map(int,stdin.readline().split()):
    if i != -1:
        rootNodes.remove(n) #부모가 주어진 노드는 root아님
        Tree[i].append(n)
    n+=1
toRemoveNode = int(stdin.readline().rstrip())

leafNodes = 0
visited = [False] * N
def dfs(n):
    global leafNodes
    visited[n] = True
    if n == toRemoveNode: return
    #자식이 없거나, 하나 있는데 지워진 노드일때 == 리프노드
    if len(Tree[n]) == 0 or (len(Tree[n]) == 1 and Tree[n][0] == toRemoveNode):
        leafNodes += 1
        return
    #아닐시
    for v in Tree[n]:
        if visited[v] == False:
            dfs(v)

for r in rootNodes:
    dfs(r)
print(leafNodes)