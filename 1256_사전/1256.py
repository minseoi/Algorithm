#https://www.acmicpc.net/problem/1256

import math

def comb(a,z):
    return int(math.factorial(a+z) / (math.factorial(a) * math.factorial(z)))


N, M, K = map(int,input().split())

nIndex = [i+N for i in range(M)]
if comb(a = N, z = M) < K:
    print(-1)
else:
    for i in range(N+M):
        if N==0 or M==0:
            break

        value = comb(a= N-1, z = M)
        if K <= value: #맨 앞자리가 a일때
            print('a',end='')
            N-=1
        else:          #맨 앞자리가 z일때
            print('z',end='')
            M-=1
            K -= value
    #남은 z나 a 추가
    print("a"*N + "z"*M)