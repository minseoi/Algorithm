#https://www.acmicpc.net/problem/14720

def NextTarget():
  global target
  if target >= 2:
    target =0
  else: target+=1

N = int(input())
milkShopList = list(map(int,input().split()))
target = 0
result = 0

for m in milkShopList:
  if m == target:
    result += 1
    NextTarget()
  else:
    continue

print(result)