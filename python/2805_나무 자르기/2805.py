#https://www.acmicpc.net/problem/2805

from sys import stdin

def CuttingTrees(trees, h):
    result = 0
    for t in trees:
        if t > h:
            result += t-h
    return result

N, M = map(int,stdin.readline().split())
trees = list(map(int,stdin.readline().split()))

start = 0
end = max(trees)
mid = 0
highest = 0
while start <= end:
    mid = (start + end) // 2
    cutTree = CuttingTrees(trees,mid)
    if cutTree >= M:
        start = mid+1
        highest = max(mid,highest)
    elif cutTree < M:
        end = mid-1

print(highest)