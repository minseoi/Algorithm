#https://www.acmicpc.net/problem/1654

from sys import stdin

INF = int(10e6)
def CuttingLines(lines, len):
    if len==0: return INF
    result = 0
    for l in lines:
        result += l // len
    return result

K, N = map(int,stdin.readline().split())
lines = [int(stdin.readline().rstrip()) for _ in range(K)]

start = 0
end = max(lines)
mid = 0
longest = 0
while start <= end:
    mid = (start + end) // 2
    cutLine = CuttingLines(lines,mid)
    if cutLine >= N:
        start = mid+1
        longest = max(mid,longest)
    elif cutLine < N:
        end = mid-1

print(longest)