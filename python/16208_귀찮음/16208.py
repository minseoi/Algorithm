#https://www.acmicpc.net/problem/16208

n = int(input())
nList = list(map(int,input().split()))
nList.sort()
sumOfList = sum(nList)

result = 0
for i in nList:
  sumOfList -= i
  result += i * sumOfList
print(result)