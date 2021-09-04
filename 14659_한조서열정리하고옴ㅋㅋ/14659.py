#https://www.acmicpc.net/problem/14659

import sys

N = int(sys.stdin.readline())
height = list(map(int,sys.stdin.readline().split()))
maxkillcount=0
count=0
hBong = 0

for h in height:
  if(h > hBong):
    hBong = h
    count=0
  else:
    count+=1
  maxkillcount = max(maxkillcount,count)

print(maxkillcount)