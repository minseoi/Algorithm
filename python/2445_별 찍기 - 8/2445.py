#https://www.acmicpc.net/problem/2445

N = int(input())
countStar= 0
countBlank=0
for i in range(2*N - 1):
    if i < N:
        countStar += 1
    else:
        countStar -= 1
    countBlank = 2*N - 2*countStar
    print('*'*countStar + ' '*countBlank + '*'*countStar)
