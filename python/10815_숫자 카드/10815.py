#https://www.acmicpc.net/problem/10815

from sys import stdin

hash = dict()
N = int(stdin.readline().rstrip())
N_list = list(map(int,stdin.readline().split()))
for n in N_list:
    if n in hash:
        hash[n] +=1
    else:
        hash[n] = 1

M = int(stdin.readline().rstrip())
M_list = list(map(int,stdin.readline().split()))
result = []
for m in M_list:
    if m in hash:
        result.append(hash[m])
    else:
        result.append(0)
print(*result)