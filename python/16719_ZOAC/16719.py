#https://www.acmicpc.net/problem/16719

string = list(input())
selected = [False]*len(string)

def printString():
    for s in range(len(selected)):
        if selected[s] == True:
            print(string[s],end='')
    print()

def ZOAC(_str, startIndex):
    if len(_str) < 1: return
    c= min(_str)
    cIndex = _str.index(c)
    selected[startIndex + cIndex] = True
    printString()
    if startIndex+cIndex+1 < len(string):
        ZOAC(_str[cIndex+1:],startIndex + cIndex+1)
    ZOAC(_str[:cIndex],startIndex)

ZOAC(string,0)