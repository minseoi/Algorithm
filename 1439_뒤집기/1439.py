#https://www.acmicpc.net/problem/1439

S = input()
s = ""

s += S[0]
previousC = S[0]
for c in S[1:]:
    if c == previousC:
        continue

    s += c
    if c == '0':
        previousC = c
    elif c == '1':
        previousC = c

print(min(s.count('0'),s.count('1')))