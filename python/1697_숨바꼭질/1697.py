#https://www.acmicpc.net/problem/1697

from sys import stdin
from collections import deque

N, K = map(int,stdin.readline().split())
timeTo = [0] * 100_001

def bfs():
    queue = deque()
    queue.append(N)
    while queue:
        x = queue.popleft()
        if x == K:
            break
        for dx in (x-1, x+1, 2*x):
            if 0 <= dx <= 100_000:
                if timeTo[dx] == 0:
                    timeTo[dx] = timeTo[x]+1
                    queue.append(dx)

bfs()
print(timeTo[K])