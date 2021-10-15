#https://www.acmicpc.net/problem/2156

from sys import stdin

n = int(stdin.readline().rstrip())
wines = []
for i in range(n):
    wines.append(int(stdin.readline().rstrip()))
dp = [0] * n

dp[0] = wines[0]
if n > 1:
    dp[1] = wines[0] + wines[1]
if n > 2:
    dp[2] = max(max(wines[0]+ wines[2], wines[1] + wines[2]),dp[1])

for i in range(3,n):
    dp[i] = max(dp[i-2] + wines[i], dp[i-3] + wines[i-1] + wines[i])
    dp[i] = max(dp[i], dp[i-1])

print(dp[n-1])