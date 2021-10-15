#https://www.acmicpc.net/problem/2447

N = int(input())
Map = [[' ']*N for _ in range(N)]

def Star(x,y,num):
    if num == 1:
        Map[y][x] = '*'
    else:
        space = num // 3
        for _y in range(3):
            for _x in range(3):
                if _x==1 and _y==1: continue
                Star(x+(_x * space),y+(_y * space),space)
Star(0,0,N)

for y in Map:
    print(''.join(y))