#https://www.acmicpc.net/problem/5086

from sys import stdin

def IsFacor(x,y):
    n = (y//x) * x
    if n==y:
        return True
    else:
        return False

def IsMultiple(x,y):
    n = (x//y) * y
    if n==x:
        return True
    else:
        return False

while True:
    x, y = map(int,stdin.readline().split())
    if x==0 and y==0:
        break
    if IsFacor(x,y):
        print('factor')
    elif IsMultiple(x,y):
        print('multiple')
    else:
        print('neither')