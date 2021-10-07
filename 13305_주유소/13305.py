#https://www.acmicpc.net/problem/13305

from sys import stdin

N = int(stdin.readline().rstrip())
distBetweenCity = list(map(int,stdin.readline().split()))
oilPrice = list(map(int,stdin.readline().split()))
result = 0

cheapestOilPrice = 1_000_000_001
for i in range(N-1):
    cheapestOilPrice = min(oilPrice[i], cheapestOilPrice)
    result += distBetweenCity[i] * cheapestOilPrice
print(result)