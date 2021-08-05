#https://www.acmicpc.net/problem/2581

M = int(input())
N = int(input())

primeNums = [i for i in range(N+1)]
for i in range(len(primeNums)):
    if primeNums[i] == 0 or primeNums[i] == 1:
        continue

    _i = i*2
    count = 3
    while _i <= len(primeNums)-1:
        primeNums[_i] = 0
        _i = i * count
        count+=1

existPrimNum = False
sum = 0
minNum = 10001
for n in primeNums[M:]:
    if n!=0 and n!=1:
        sum += n
        minNum = min(minNum,n)
        if existPrimNum == False:
            existPrimNum = True

if existPrimNum:
    print(sum)
    print(minNum)
else:
    print('-1')