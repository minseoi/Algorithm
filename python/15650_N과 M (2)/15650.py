#https://www.acmicpc.net/problem/15650

from sys import stdin

N, M = map(int,stdin.readline().split())

li = list()
def Comb(N,M,n=1,depth=0):
    if depth == M:
        for i in li:
            print(i,end=' ')
        print()
        return
    for i in range(n,N+1):
        li.append(i)
        Comb(N,M,i+1,depth+1)
        li.pop()

Comb(N,M)