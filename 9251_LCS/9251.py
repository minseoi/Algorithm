#https://www.acmicpc.net/problem/9251

from sys import stdin

s1 = ' '+stdin.readline().rstrip()
s2 = ' '+stdin.readline().rstrip()
dp = [[0] * len(s1) for _ in range(len(s2))]

for i2 in range(1,len(s2)):
    for i1 in range(1,len(s1)):
        if s1[i1] == s2[i2]:
            dp[i2][i1] = dp[i2-1][i1-1] + 1
        elif s1[i1] != s2[i2]:
            dp[i2][i1] = max(dp[i2-1][i1], dp[i2][i1-1])

print(dp[-1][-1])