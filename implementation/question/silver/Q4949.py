## 균형잡힌 세상 (실버 4)

import sys

while 1:
    s = sys.stdin.readline().rstrip()
    if s == '.': break
    stack = []
    
    for i in s:
        if i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ']':
            if stack and stack[-1] =='[':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == '(' or i == '[':
            stack.append(i)
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
        

    