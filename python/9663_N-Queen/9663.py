#https://www.acmicpc.net/problem/9663

N = int(input())
count = 0

queens = [int(1e2)]*N
def PutQueen(row):
    global count
    for c in range(N):
        if c in queens: continue

        queens[row] = c
        isAvailable = True

        for i in range(N):
            if i == row: continue
            diff = row-i
            if queens[i] == c + diff or queens[i] == c + (-diff):
                isAvailable = False
                break
        if not isAvailable:
            continue

        if row != N-1:
            PutQueen(row+1)
        elif row == N-1:
            count += 1
    queens[row] = int(1e2)
    
PutQueen(0)
print(count)