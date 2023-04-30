#https://www.acmicpc.net/problem/18870

from sys import stdin

N = int(stdin.readline().rstrip())
originX = list(map(int,stdin.readline().split()))
X = sorted(list(set(originX)))
dic = dict()
for i in range(len(X)):
    dic[X[i]] = i

for x in originX:
    print(dic[x],end=' ')