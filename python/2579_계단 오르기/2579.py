#https://www.acmicpc.net/problem/2579

from sys import stdin

n = int(stdin.readline().rstrip())
stair = [0]
for i in range(n):
    stair.append(int(stdin.readline().rstrip()))
dp = [0] * (n+1)
dp[1] = stair[1]
if n >= 2:
    dp[2] = stair[1] + stair[2]

for i in range(3,n+1):
    dp[i] = max( dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i] )

print(dp[n])