#https://www.acmicpc.net/problem/7576

from collections import deque

M, N = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(N)]

#up, right, down, left
dx = (0,+1,0,-1)
dy = (-1,0,+1,0)

def bfs(box):
    count_day = 0
    todaysTarget = 0
    tomorrowTarget = 0
    queue = deque()
    for n in range(N):
        for m in range(M):
            if box[n][m] == 1:
                queue.append( (n,m) )
                todaysTarget += 1
    while queue:
        v = queue.popleft()
        #4방향
        for i in range(4):
            new_n = v[0] + dy[i]
            new_m = v[1] + dx[i]
            if 0<= new_n < N and 0<= new_m < M:
                if box[new_n][new_m] == 0:
                    queue.append((new_n,new_m))
                    box[new_n][new_m] = 1
                    tomorrowTarget += 1

        todaysTarget -= 1
        if todaysTarget == 0:
            count_day += 1
            todaysTarget = tomorrowTarget
            tomorrowTarget = 0
    #더 채울게 없는지 확인하는 마지막날 제외.
    return count_day -1

result = bfs(box)
for n in range(N):
    for m in range(M):
        if box[n][m] == 0:
            result = -1
print(result)