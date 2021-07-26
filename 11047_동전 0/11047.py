#https://www.acmicpc.net/problem/11047

N, K = map(int,input().split())
Coins = []

for i in range(N):
    Coins.append(int(input()))

count = 0
for coin in reversed(Coins):
    count += K // coin
    K %= coin

print(count)
