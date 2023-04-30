#https://www.acmicpc.net/problem/1874

n = int(input())
stack = []
result = []
count = 0

for i in range(n):
    target = int(input())
    while target > count:
        count += 1
        stack.append(count)
        result.append('+')
    if stack[-1] == target:
        stack.pop()
        result.append('-')
    else:
        result = ['NO']
        break

print('\n'.join(result))