#https://www.acmicpc.net/problem/2747

fiboList = [0, 1] + [-1 for _ in range(44)]

def Fibonacci(n):
    if fiboList[n] > -1:
        return fiboList[n]
    else:
        result = Fibonacci(n-1) + Fibonacci(n-2)
        fiboList[n] = result
        return result

n = int(input())
print(Fibonacci(n))