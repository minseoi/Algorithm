#https://www.acmicpc.net/problem/17298

from sys import stdin

N = int(stdin.readline().rstrip())
A = list(map(int,stdin.readline().split()))
NGE = [-1]*N

stack = []
for i in range(N):
    while stack and A[stack[-1]] < A[i]:
            idx = stack.pop()
            NGE[idx] = A[i]
    stack.append(i)

print(*NGE)