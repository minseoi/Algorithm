#https://www.acmicpc.net/problem/11650

from sys import stdin

N = int(input())
posList = [list(map(int,stdin.readline().split())) for _ in range(N)]
posList.sort(key = lambda x:(x[0], x[1]))

for pos in posList:
    print(pos[0],pos[1])