#https://www.acmicpc.net/problem/7567

bowls = list(input())
result = 10
for i in range(1,len(bowls)):
    if bowls[i-1] == bowls[i]:
        result += 5
    else:
        result += 10
print(result)