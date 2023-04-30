#https://www.acmicpc.net/problem/1074

from sys import stdin

N, r, c = map(int,stdin.readline().split())

count = 0
def Z(_r,_c, size):
    if size == 1: return
    global count
    half_size = size // 2
    if _r< half_size and _c >= half_size:
        #1사분면
        count += (size//2) * (size//2)
        Z(_r,_c-half_size,half_size)
    elif _r < half_size and _c < half_size:
        #2사분면
        Z(_r,_c,half_size)
    elif _r >= half_size and _c < half_size:
        #3사분면
        count += (size) * (size//2)
        Z(_r-half_size,_c,half_size)
    elif _r >= half_size and _c >= half_size:
        #4사분면
        count += (size) * (size//2) + (size//2)*(size//2)
        Z(_r-half_size,_c-half_size,half_size)

Z(r,c, 2**N)
print(count)