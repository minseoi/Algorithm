#https://www.acmicpc.net/problem/15652

from sys import stdin

N, M = map(int,stdin.readline().split())

li = list()
def Comb(N,M,start = 1, depth=0):
    if depth == M:
        for i in li:
            print(i,end=' ')
        print()
        return
    for i in range(start,N+1):
        li.append(i)
        Comb(N,M,i, depth+1)
        li.pop()

Comb(N,M)