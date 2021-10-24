#https://www.acmicpc.net/problem/14501

from sys import stdin
from itertools import combinations

N = int(stdin.readline().rstrip())
N_list = [i for i in range(N)]
T = [0] * N
P = [0] * N

for i in range(N):
    T[i], P[i] = map(int,stdin.readline().split())

result = 0
for i in range(1,N+1):
    for j in list(combinations(N_list,i)):
        check = [False] * N
        tempResult = 0
        for k in j:
            if check[k] == False and k+T[k] <= N:
                tempResult += P[k]
                for d in range(T[k]):
                    check[k+d] = True
            else:
                break
        result = max(result, tempResult)
    
print(result)