#https://www.acmicpc.net/problem/1946

from sys import stdin

T = int(input())
for _ in range(T):
    N = int(input())
    count = 0;

    ranks = [list(map(int,stdin.readline().split())) for _ in range(N)]
    ranks.sort(key= lambda x : x[0])
    baseScore = 100001

    for r in ranks:
        if r[1] < baseScore:
            baseScore = r[1]
            count += 1
            if baseScore == 1:
                break;
    print(count)