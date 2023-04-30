#https://www.acmicpc.net/problem/2748

from sys import stdin

n = int(stdin.readline().rstrip())
dp = dict()

dp[0] = 0
dp[1] = 1

def fibonacci(n):
    if n not in dp:
        dp[n] = fibonacci(n-1) + fibonacci(n-2)
    return dp[n]

print(fibonacci(n))