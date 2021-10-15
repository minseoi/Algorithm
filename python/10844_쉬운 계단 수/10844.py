#https://www.acmicpc.net/problem/10844

from sys import stdin

N = int(stdin.readline().rstrip())
dp = [[0]*N for _ in range(10)]

def StairNumber(i, depth=0):
    if i<0 or 9<i:
        return 0
    if depth == N-1:
        return 1
    if dp[i][depth] == 0:
        dp[i][depth] = StairNumber(i-1,depth+1) + StairNumber(i+1,depth+1) % 1_000_000_000
    
    return dp[i][depth]

result = 0
for i in range(1,10):
    result += StairNumber(i)
print(result % 1_000_000_000)