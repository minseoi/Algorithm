#https://www.acmicpc.net/problem/14891

from collections import deque
from types import GetSetDescriptorType

Gears = deque()
Gears.append([])
for i in range(4):
    Gears.append(list(map(int,list(input()))))

def RotateClockwise(gear):
    temp = gear.pop()
    gear.insert(0,temp)

def RotateCounterColockwise(gear):
    temp = gear[0]
    del(gear[0])
    gear.append(temp)

def RotateGear(num, Rdir, rotated):
    rotated[num] = True

    if num-1 >= 1 and rotated[num-1] == False:
        if Gears[num][6] != Gears[num-1][2]:
            RotateGear(num-1, -Rdir, rotated)
    if num+1 <= 4 and rotated[num+1] == False:
        if Gears[num][2] != Gears[num+1][6]:
            RotateGear(num+1, -Rdir, rotated)
    
    if Rdir == 1:
        RotateClockwise(Gears[num])
    elif Rdir == -1:
        RotateCounterColockwise(Gears[num])

K = int(input())
for k in range(K):
    num, Rdir = map(int,input().split())
    rotated = [False] * 5
    RotateGear(num,Rdir,rotated)

score = 0
for i in range(1,5):
    if Gears[i][0] == 1:
        score += pow(2,i-1)
print(score)