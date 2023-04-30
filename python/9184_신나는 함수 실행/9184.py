#https://www.acmicpc.net/problem/9184

from sys import stdin

dic = dict()

def w(a, b, c):
    if (a,b,c) in dic:
        return dic[(a,b,c)]
    else:
        if a<=0 or b<=0 or c<=0:
            dic[(a,b,c)] = result = 1
        elif a>20 or b>20 or c>20:
            dic[(a,b,c)] = result = w(20, 20, 20)
        elif a<b and b<c:
            dic[(a,b,c)] = result = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        else:
            dic[(a,b,c)] = result = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

        return result

while True:
    a, b, c = map(int,stdin.readline().split())
    if a== -1 and b==-1 and c==-1:
        break
    result = w(a,b,c)
    print(f"w({a}, {b}, {c}) = {result}")