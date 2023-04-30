#https://www.acmicpc.net/problem/4948

primeNums = [i for i in range((123456 * 2)+1)]
primeNums[1] = 0
maxN = 0

while True:
    n = int(input())
    if n == 0:
        break
    
    if n > maxN:
        maxN = n
        for i in range(2,(2*n)+1):
            for j in range(i * 2,(2*n+1),i):
                primeNums[j] = 0
    sum = 0
    for i in range(n+1,(2*n)+1):
        sum += 1 if primeNums[i] != 0 else 0
    print(sum)