#https://www.acmicpc.net/problem/10867

from sys import stdin

N = int(input())
numList = list(set(map(int,stdin.readline().split())))
numList.sort()

for n in numList:
    print(n,end=' ')