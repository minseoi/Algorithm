#https://www.acmicpc.net/problem/1339

from sys import stdin

N = int(stdin.readline().rstrip())
longestLength = 0
words = []
charWeight = [0]*26

for n in range(N):
    word = stdin.readline().rstrip()
    wordLength = len(word)
    for i in range(wordLength):
        charWeight[ord(word[i]) - ord('A')] += pow(10,wordLength-1 -i )
    words.append(word)

count = 9
result = 0
while True:
    maxWeight = max(charWeight)
    charWeight[charWeight.index(maxWeight)] = 0
    if maxWeight == 0: break

    result += maxWeight * count
    count-=1
print(result)