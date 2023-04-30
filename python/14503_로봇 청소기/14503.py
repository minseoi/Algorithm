#https://www.acmicpc.net/problem/14503

N, M = map(int,input().split())
currentPoxY, currentPosX, currentDir = map(int,input().split())
area = [list(map(int,input().split())) for _ in range(N)]
count = 0
dirX = (0,1,0,-1)
dirY = (-1,0,1,0)

while True:
    if area[currentPoxY][currentPosX] == 0:
        area[currentPoxY][currentPosX] = 2 #현재위치 청소
        count += 1
    isFind = False
    for i in range(4):
        currentDir -= 1
        if currentDir < 0: currentDir += 4
        frontY = currentPoxY + dirY[currentDir]
        frontX = currentPosX + dirX[currentDir]
        if area[frontY][frontX] == 0:
            currentPoxY = frontY
            currentPosX = frontX
            isFind = True
            break
        else:
            continue
    if isFind: #회전중 앞으로 이동해 break로 빠져나온 경우
        continue
    else: #4방향 다 탐색해도 막혔거나, 벽인 경우
        backY = currentPoxY - dirY[currentDir]
        backX = currentPosX - dirX[currentDir]
        if area[backY][backX] != 1:
            currentPoxY = backY
            currentPosX = backX
            continue
        else:
            break
print(count)