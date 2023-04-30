#https://www.acmicpc.net/problem/1193

X = int(input())
x=1
level = 1
while (x + level) <= X:
    x += level
    level += 1

if(level % 2 == 0): #짝수일때
    x_result = [1,level]
    while x != X: #좌하 방향으로 탐색
        x+=1
        x_result[0] += 1
        x_result[1] -= 1
else: #홀수일때
    x_result = [level,1]
    while x != X: #우상 방향으로 탐색
        x+=1
        x_result[0] -= 1
        x_result[1] += 1

print("{0}/{1}".format(x_result[0],x_result[1]))