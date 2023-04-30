#https://www.acmicpc.net/problem/1120

A,B= input().split()
lenDiff = len(B) - len(A)
minDiff = 50

for i in range(lenDiff+1):
    minValue = 0
    for c in range(len(A)):
        if A[c] != B[c] and A[c] != ' ':
            minValue += 1
    if minValue < minDiff:
        minDiff = minValue
    A = ' '+A
print(minDiff)