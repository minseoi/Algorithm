#https://www.acmicpc.net/problem/1931

from sys import stdin

N = int(input())
count = 0
meetings = [list(map(int,stdin.readline().split())) for _ in range(N)]
meetings.sort(key=lambda x : (x[1], x[0]))

time_end = 0
for m in meetings:
    if m[0] >= time_end:
        time_end = m[1]
        count += 1

print(count)