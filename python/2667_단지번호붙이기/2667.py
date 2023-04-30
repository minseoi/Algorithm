#https://www.acmicpc.net/problem/2667

N = int(input())
Map = [list(input()) for _ in range(N)]
NumOfHouses = []

def dfs(Map,x,y):
    count = 0
    if x>=0 and x<N and y>=0 and y<N:
        if Map[y][x] == '1':
            Map[y][x] = '0'
            count = 1
            count += dfs(Map,x+1,y)
            count += dfs(Map,x,y+1)
            count += dfs(Map,x-1,y)
            count += dfs(Map,x,y-1)
    return count

for y in range(N):
    for x in range(N):
        c = dfs(Map,x,y)
        if c != 0:
            NumOfHouses.append(c)
            c=0

NumOfHouses.sort()
print(len(NumOfHouses))
for n in NumOfHouses:
    print(n)