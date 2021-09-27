#https://www.acmicpc.net/problem/9461

from sys import stdin

T = int(stdin.readline().rstrip())
dp = [0,1,1,1,2,2,3,4,5,7,9] + [-1]*(101 - 11)

def P(n):
    if dp[n] == -1:
        dp[n] = P(n-1) + P(n-5)
    return dp[n]

for t in range(T):
    N = int(stdin.readline().rstrip())
    print(P(N))