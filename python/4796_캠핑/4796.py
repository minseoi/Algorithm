#https://www.acmicpc.net/problem/4796

from sys import stdin

caseCount = 1
while True:
    L, P, V = map(int,stdin.readline().split())
    if L==0 and P==0 and V==0:
        break

    result = (V//P)*L + (V%P if V%P <= L else L)
    print("Case {0}: {1}".format(caseCount,result))
    caseCount+=1