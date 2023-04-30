#https://www.acmicpc.net/problem/1713

from sys import stdin

def IsinFrame(value, frame):
    for i in frame:
        if i["id"] == value:
            return True
    return False

N = int(stdin.readline().rstrip())
R = int(stdin.readline().rstrip())
#1. 학생들이 추천을 시작하기 전에 모든 사진틀은 비어있다.
frame = []

time = 0
for r in map(int,stdin.readline().split()):
    if not IsinFrame(r,frame):
        #3. 비어있는 사진틀이 없는 경우에는 추천받은 횟수가 가장 적은 학생의 사진을 삭제한다.
        #   추천받은 횟수가 가장 적은 학생이 두 명 이상일 경우에는 가장 오래된 사진을 삭제한다.
        if N == len(frame):
            isTowOrMore = False
            minIndex = 0
            for i in range(1, len(frame)):
                if frame[i]["rc"] < frame[minIndex]["rc"]:
                    minIndex = i
                    isTowOrMore = False
                elif frame[i]["rc"] == frame[minIndex]["rc"]:
                    isTowOrMore = True

            odderIndex = minIndex
            if isTowOrMore:
                for i in range(len(frame)):
                    if frame[i]["rc"] == frame[minIndex]["rc"]: #추천수 제일 작은 사진 중에
                        if frame[i]["tm"] < frame[odderIndex]["tm"]: #제일 오래된 사진 선택
                            odderIndex = i
                del frame[odderIndex]
            else:
                del frame[minIndex]

        #2.어떤 학생이 특정 학생을 추천하면, 추천받은 학생의 사진이 반드시 사진틀에 게시되어야 한다.
        frame.append({"id":r, "rc":0, "tm":time})
        time+=1
    else:
        #4. 현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우에는 추천받은 횟수만 증가시킨다.
        for i in range(len(frame)):
            if frame[i]["id"] == r:
                frame[i]["rc"] += 1
                break

result = []
for i in frame:
    result.append(i["id"])
result.sort()
print( ' '.join(map(str,result)) )