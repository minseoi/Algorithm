#https://www.acmicpc.net/problem/1744

from sys import stdin

N = int(stdin.readline().rstrip())
nums = [int(stdin.readline().rstrip()) for _ in range(N)]
nums.sort()

tempStack = []
while True:
    if(len(nums) < 2): break
    n1 = nums.pop()
    n2 = nums.pop()
    if (n1 <= 1) or (n2 <= 1):
        nums.append(n2)
        nums.append(n1)
        break
    else:
        tempStack.append(n1 * n2)
nums.extend(tempStack)

nums.sort(reverse=True)
tempStack = []
while True:
    if(len(nums) < 2): break
    n1 = nums.pop()
    n2 = nums.pop()
    if (n1 > 0) or (n2 > 0):
        nums.append(n2)
        nums.append(n1)
        break
    else:
        tempStack.append(n1 * n2)
nums.extend(tempStack)

print(sum(nums))