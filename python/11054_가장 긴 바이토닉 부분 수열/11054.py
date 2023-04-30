#https://www.acmicpc.net/problem/11054

from sys import stdin

N = int(stdin.readline().rstrip())
A = list(map(int,stdin.readline().split()))

tempResult=0
dp1 = [1] * N
dp2 = [1] * N
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp1[i] = max(dp1[j]+1, dp1[i])
for i in range(N-1,-1,-1):
    for j in range(N-1, i, -1):
        if A[j] < A[i]:
            dp2[i] = max(dp2[j]+1, dp2[i])

result = 0
for i in range(N):
    result = max(dp1[i] + dp2[i], result)
print(result-1)