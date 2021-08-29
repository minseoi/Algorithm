#https://www.acmicpc.net/problem/4949

from sys import stdin

while True:
    str = stdin.readline().rstrip()
    if str == '.': break
    stack = []
    isBalanced = True

    for c in str:
        if c in ('(','['):
            stack.append(c)
        elif c in (')',']'):
            if len(stack) == 0:
                isBalanced = False
                break

            if c == ')' and stack[-1] == '(':
                stack.pop()
            elif c == ']' and stack[-1] =='[':
                stack.pop()
            else:
                isBalanced = False
                break
    if len(stack) != 0:
        isBalanced = False

    if isBalanced:
        print("yes")
    else:
        print("no")
