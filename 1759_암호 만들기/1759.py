#https://www.acmicpc.net/problem/1759

#조합 구현
combReturnList = []
def Combination(l,r, ans=[], isRecursion = False):
    global combReturnList
    if not isRecursion: combReturnList = [] #초기화

    if r == 0:
        combReturnList.append(ans[:])
        ans.pop()
    else:
        for i in range(len(l) - r+1):
            ans.append(l[i])
            Combination(l[i+1:], r-1, ans, True)
        if ans:
            ans.pop()
    
    if not isRecursion:
        return combReturnList
####################################################

L, C = map(int,input().split())
chars = list(input().split())
vowel = ('a','e','i','o','u')

#모음과 자음 따로 모아두기
vowelChars =[]
consonantChars = []
for c in chars:
    if c in vowel:
        vowelChars.append(c)
    else:
        consonantChars.append(c)

#자음과 모음 개수 경우의수 구하기
#(3 = 최소모음1 + 최소자음2)
vowelCount = 1
consonantCount = 2
count = L - (vowelCount + consonantCount)

vowelCount += count
maxVowelCount = len(vowelChars)
if vowelCount > maxVowelCount:
    remainder = vowelCount - maxVowelCount
    vowelCount -= remainder
    consonantCount += remainder

result = []
while vowelCount >= 1:
    Vcomb = Combination(vowelChars,vowelCount)
    Ccomb = Combination(consonantChars,consonantCount)
    
    for v in Vcomb:
        for c in Ccomb:
            password = v+c
            password.sort()
            result.append(''.join(password))

    vowelCount -= 1
    consonantCount += 1

result.sort()
for r in result:
    print(r)