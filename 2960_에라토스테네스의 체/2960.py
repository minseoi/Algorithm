#https://www.acmicpc.net/problem/2960

from sys import stdin

N, K = map(int,stdin.readline().split())
isPrime = [False, False] + [True]*(N-1)
counter = 0

for i in range(2,N+1):
    if isPrime[i] and counter < K:
        for j in range(i,N+1,i):
            if isPrime[j]:
                isPrime[j] = False
                counter += 1
                if counter == K:
                    print(j)
                    break