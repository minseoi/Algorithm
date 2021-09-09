#https://www.acmicpc.net/problem/11053

from sys import stdin

N = int(stdin.readline().rstrip())
A = list(map(int,stdin.readline().split()))

count = [1] * N
for i in range(1,N):
    for j in range(i):
        if A[j] < A[i]:
            count[i] = max(count[j] + 1,count[i])

print(max(count))