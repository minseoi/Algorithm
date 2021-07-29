#https://www.acmicpc.net/problem/1094

sticks = [64]
targetLen = int(input())

while(sum(sticks) != targetLen):
    shortestStick = sticks[-1]
    sticks.append(shortestStick // 2)
    sticks.remove(shortestStick)
    if(sum(sticks) < targetLen):
        sticks.append(shortestStick // 2)

print(len(sticks))