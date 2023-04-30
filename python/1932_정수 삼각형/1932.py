#https://www.acmicpc.net/problem/1932

from sys import stdin

n = int(stdin.readline().rstrip())
triangle = [[]]
for _ in range(n):
    triangle.append(list(map(int,stdin.readline().split())))
dp = [[]]
for i in range(1,n+1):
    dp.append([-1] * i)

def search(idx=0, depth=1):
    global maxSum
    if depth == n:
        return triangle[depth][idx]
    if dp[depth][idx] != -1:
        return dp[depth][idx]
    
    myValue = triangle[depth][idx]
    maxSum = 0
    for i in range(2):
        maxSum = max(maxSum, myValue + search(idx+i ,depth+1))
    dp[depth][idx] = maxSum
    return maxSum

print(search())