#https://www.acmicpc.net/problem/2309

from itertools import combinations

dwarfs = []
for i in range(9):
    dwarfs.append(int(input()))

comb = combinations(dwarfs,7)
for c in comb:
    if sum(c) == 100:
        c = list(c)
        c.sort()
        for _c in c:
            print(_c)
        break