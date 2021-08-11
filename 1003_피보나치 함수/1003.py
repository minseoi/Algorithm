#https://www.acmicpc.net/problem/1003

countList = [
    [1,0]+[-1 for _ in range(39)],
    [0,1]+[-1 for _ in range(39)]
]

count0 = 0
count1 = 0
def MiniFibo(n):
    global count0; global count1
    if countList[0][n] != -1 and countList[1][n] != -1:
        count0 += countList[0][n]
        count1 += countList[1][n]
    else:
        MiniFibo(n-1); MiniFibo(n-2)
        countList[0][n] = count0
        countList[1][n] = count1

T = int(input())
for t in range(T,0,-1):
    N = int(input())
    MiniFibo(N)
    print(count0,count1)
    count0=0; count1=0
