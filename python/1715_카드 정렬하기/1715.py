#https://www.acmicpc.net/problem/1715

import heapq

N = int(input())
cards=[]
count = 0

for n in range(N):
    heapq.heappush(cards,int(input()))

while len(cards) > 1:
    sum = heapq.heappop(cards) + heapq.heappop(cards)
    count += sum
    heapq.heappush(cards,sum)
print(count)