#https://www.acmicpc.net/problem/9020

numberRange = 10000
isPrimeNumber = [False,False] + [True for _ in range(numberRange -1)]
for i in range(2,int(numberRange ** 0.5) + 1):
    if isPrimeNumber[i]:
        for j in range(i*2,numberRange+1,i):
            isPrimeNumber[j] = False

T = int(input())

for t in range(T):
    n = int(input())
    min = n//2
    max = n//2
    while not(isPrimeNumber[min] and isPrimeNumber[max]):
        min-=1
        max+=1
    print(min,max)