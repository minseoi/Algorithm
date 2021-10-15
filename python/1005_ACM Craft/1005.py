#https://www.acmicpc.net/problem/1005

from sys import stdin
from collections import deque

T = int(stdin.readline().rstrip())
for t in range(T):
    #입력부
    N, K = map(int,stdin.readline().split())
    buildDelay = [0] + list(map(int,stdin.readline().split()))
    buildTree = [[] for _ in range(N+1)]
    inDegree = [0] * (N+1)
    for k in range(K):
        n1, n2 = map(int,stdin.readline().split())
        buildTree[n1].append(n2)
        inDegree[n2] += 1
    target = int(stdin.readline().rstrip())

    #연산부
    timeToBuild = [-1] * (N+1)
    queue = deque()
    for i in range(1,N+1):
        if inDegree[i] == 0: #root
            queue.append(i)
            timeToBuild[i] = buildDelay[i]
            
    while queue:
        n = queue.popleft()
        for i in buildTree[n]:
                inDegree[i] -= 1
                timeToBuild[i] = max(timeToBuild[n] + buildDelay[i], timeToBuild[i])
                if inDegree[i] == 0:
                    queue.append(i)
    
    print(timeToBuild[target])