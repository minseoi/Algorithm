#https://www.acmicpc.net/problem/1181

N = int(input())
words = []
for n in range(N):
    word = input()
    if word not in words:
        words.append(word)

words.sort()
words.sort(key=lambda x: len(x))

for w in words:
    print(w)