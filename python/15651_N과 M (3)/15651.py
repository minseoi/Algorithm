#https://www.acmicpc.net/problem/15651

from sys import stdin

N, M = map(int,stdin.readline().split())

li = list()
def Comb(N,M,depth=0):
    if depth == M:
        for i in li:
            print(i,end=' ')
        print()
        return
    for i in range(1,N+1):
        li.append(i)
        Comb(N,M,depth+1)
        li.pop()

Comb(N,M)