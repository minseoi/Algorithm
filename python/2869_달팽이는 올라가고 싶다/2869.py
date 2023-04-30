#https://www.acmicpc.net/problem/2869

import math

A,B,V = map(int,input().split())
vPerDay = A-B
print(math.ceil((V-A) / vPerDay)+1)
