#https://www.acmicpc.net/problem/14888

from sys import stdin

N = int(stdin.readline().rstrip())
a_List = list(map(int,stdin.readline().split()))
operatorMaxCount = list(map(int,stdin.readline().split()))
operatorNowCount = [0, 0, 0, 0]
maxValue = -1_000_000_001
minValue =  1_000_000_001

def Calculate(frontOperand = a_List[0], opCount=0):
    global maxValue; global minValue
    if opCount == N-1:
        maxValue = max(maxValue, frontOperand)
        minValue = min(minValue, frontOperand)
    else:
        negativeFlag = False if frontOperand >= 0 else True
        for i in range(len(operatorMaxCount)):
            if operatorNowCount[i] < operatorMaxCount[i]:
                op = i
                operatorNowCount[op] += 1
            
                result = 0
                if op == 0:   # +
                    result = frontOperand + a_List[opCount+1]
                elif op == 1: # -
                    result = frontOperand - a_List[opCount+1]
                elif op == 2: # ×
                    result = frontOperand * a_List[opCount+1]
                elif op == 3: # ÷
                    if negativeFlag:
                        result = -((-frontOperand) // a_List[opCount+1])
                    else:
                        result = frontOperand // a_List[opCount+1]
                
                Calculate(result, opCount+1)
                operatorNowCount[op] -= 1

Calculate()
print(maxValue)
print(minValue)