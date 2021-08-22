#https://www.acmicpc.net/problem/1966

from collections import deque

T = int(input())
for t in range(T):
    N, M = map(int,input().split())
    queue = deque(list(map(int,input().split() )))
    count = 0
    while M > -1:
        value = queue.popleft()
        M -= 1
        if value < max(queue) if len(queue) > 0 else 0:
            queue.append(value)
            if M == -1:
                M = len(queue) -1
        else:
            count += 1
    print(count)