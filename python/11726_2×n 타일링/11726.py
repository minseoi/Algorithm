#https://www.acmicpc.net/problem/11726

import sys

sys.setrecursionlimit(int(1e5))
n = int(sys.stdin.readline().rstrip())
w = [0,1,2] + [-1] *(n-2)
def dp(n):
    if w[n] != -1:
        return w[n]
    else:
        w[n-1] = dp(n-1)
        w[n-2] = dp(n-2)
        return w[n-1] + w[n-2]
print(dp(n) % 10_007)