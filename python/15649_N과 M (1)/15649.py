#https://www.acmicpc.net/problem/15649

from sys import stdin

N, M = map(int,stdin.readline().split())

li = list()
def Comb(N,M,depth=0):
    if depth == M:
        for i in li:
            print(i,end=' ')
        print()
    for i in range(1,N+1):
        if i not in li:
            li.append(i)
            Comb(N,M,depth+1)
            li.pop()

Comb(N,M)