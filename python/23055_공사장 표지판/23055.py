#https://www.acmicpc.net/problem/23055

N = int(input())
sign = [[' ']*N for _ in range(N)]

for i in range(N):
    sign[i][i] = '*'
    sign[N-1-i][i] = '*'
    sign[0][i] = '*'
    sign[N-1][i] = '*'
    sign[i][0] = '*'
    sign[i][N-1] = '*'

for i in range(N):
    for j in range(N):
        print(sign[i][j],end='')
    print()