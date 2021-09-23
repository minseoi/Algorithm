#https://www.acmicpc.net/problem/2580

import sys

sudokuMap = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
blanks = list()
for r in range(9):
    for c in range(9):
        if sudokuMap[r][c] == 0:
            blanks.append((r,c))

def GetAvailableNumbers(nowR, nowC):
    nums = [i for i in range(1,10)]

    for i in range(9):
        #세로줄 검사
        if sudokuMap[i][nowC] in nums:
            nums.remove(sudokuMap[i][nowC])
        #가로줄 검사
        if sudokuMap[nowR][i] in nums:
            nums.remove(sudokuMap[nowR][i])
    #3x3블럭 검사
    _r = (nowR//3)*3
    _c = (nowC//3)*3
    for r in range(_r,_r+3):
        for c in range(_c,_c+3):
            if sudokuMap[r][c] in nums:
                nums.remove(sudokuMap[r][c])
    return nums

def PlaySudoku(blankIdx=0):
    if blankIdx == len(blanks):
        for r in sudokuMap:
            print(*r)
        exit()

    r,c = blanks[blankIdx]
    availableNumberList = GetAvailableNumbers(r,c)
    for n in availableNumberList:
        sudokuMap[r][c] = n
        PlaySudoku(blankIdx+1)
        sudokuMap[r][c] = 0

PlaySudoku()