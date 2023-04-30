#https://www.acmicpc.net/problem/1912

from sys import stdin

n = int(stdin.readline().rstrip())
sequence = list(map(int,stdin.readline().split()))
dp = [0] * n
dp[n-1] = sequence[n-1]
for i in range(n-2,-1,-1):
    if sequence[i] > dp[i+1] + sequence[i]:
        dp[i] = sequence[i]
    else:
        dp[i] = dp[i+1] + sequence[i]

print(max(dp))