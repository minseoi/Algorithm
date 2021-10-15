#https://www.acmicpc.net/problem/1904

from sys import stdin

N = int(stdin.readline().rstrip())
tiles = [0, 1, 2] + ([0] * (N -2))

for i in range(3,N+1):
    tiles[i] = (tiles[i-1] + tiles[i-2]) % 15746

print(tiles[N])