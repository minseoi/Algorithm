#https://www.acmicpc.net/problem/12865

from sys import stdin

N, K = map(int,stdin.readline().split())
stuff = []
for i in range(N):
    W, V = map(int,stdin.readline().split())
    stuff.append([W,V])
dp = [[0] * (K+1) for _ in range(N+1)]

for n in range(1,N+1):
    w = stuff[n-1][0]
    v = stuff[n-1][1]
    #가방 무게 증가 반복문
    for k in range(1,K+1):
        #가방에 넣을수 있는 무게일 때
        if w <= k:
            #최대무게 갱신
            dp[n][k] = max(dp[n-1][k], v + dp[n-1][k-w])
        #넣을수 없으면, 기존 최대무게 사용
        else:
            dp[n][k] = dp[n-1][k]

print(dp[N][K])