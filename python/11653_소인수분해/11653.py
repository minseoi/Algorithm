#https://www.acmicpc.net/problem/11653

N = int(input())
count = 2

if N != 1:
    while count <= N:
        if N % count == 0:
            N //= count
            print(count)
        else:
            count += 1
 