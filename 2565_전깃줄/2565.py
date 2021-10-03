#https://www.acmicpc.net/problem/2565

from sys import stdin

N = int(stdin.readline().rstrip())
connecting = [0] * 501
dp = [1] *501
for i in range(N):
    a, b = map(int,stdin.readline().split())
    connecting[a] = b

for i in range(1,501):
    if connecting[i] == 0: continue
    for j in range(1,i):
        if connecting[j] == 0: continue
        if connecting[j] < connecting[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))