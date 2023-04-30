#https://www.acmicpc.net/problem/1789

S = int(input())
N = 0
s=0
p=1

while s < S:
    s += p
    p += 1
    N += 1
if s > S:
    N -= 1

print(N)