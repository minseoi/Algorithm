#https://www.acmicpc.net/problem/10816

#이분탐색을 사용하여 해결
from sys import stdin

N = int(stdin.readline().rstrip())
N_list = list(map(int,stdin.readline().split()))
M = int(stdin.readline().rstrip())
M_list = list(map(int,stdin.readline().split()))
N_list.sort()

def LowerBound(n):
    start = 0
    end = N
    while start < end:
        half = (start+end)//2
        if N_list[half] >= n:
            end = half
        elif N_list[half] < n:
            start = half + 1
    return start

def UpperBound(n):
    start = 0
    end = N
    while start < end:
        half = (start+end)//2
        if N_list[half] > n:
            end = half
        elif N_list[half] <= n:
            start = half+1
    return start

for m in M_list:
    lowerIndex = LowerBound(m)
    upperIndex = UpperBound(m)
    print(upperIndex - lowerIndex, end=' ')