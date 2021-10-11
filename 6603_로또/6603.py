#https://www.acmicpc.net/problem/6603

from sys import stdin

lottoNumbers = []
def Lotto(s,s_size,idx=0,depth=0):
    if depth == 6:
        print(*lottoNumbers)
    else:
        for i in range(idx,s_size-5+depth):
            lottoNumbers.append(s[i])
            Lotto(s,len(s),i+1,depth+1)
            lottoNumbers.pop()

while True:
    inputValue = list(map(int,stdin.readline().split()))
    k = inputValue[0]
    if k == 0:
        break
    S = inputValue[1:]
    Lotto(S,len(S))
    print()
