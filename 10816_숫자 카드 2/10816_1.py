#https://www.acmicpc.net/problem/10816

#Hash를 사용하여 해결
from sys import stdin

N = int(stdin.readline().rstrip())
N_list = list(map(int,stdin.readline().split()))
M = int(stdin.readline().rstrip())
M_list = list(map(int,stdin.readline().split()))
N_hash = dict()

for n in N_list:
    if n in N_hash:
        N_hash[n] += 1
    else:
        N_hash[n] = 1

for m in M_list:
    if m in N_hash:
        print(N_hash[m],end=' ')
    else:
        print('0',end=' ')