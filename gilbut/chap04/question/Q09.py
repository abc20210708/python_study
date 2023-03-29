## 짝지어 제거하기 *

'''
순차적으로 입력을 받으면서 알파벳 쌍이 만들어지면
해당 부분을 먼저 제거하는 방식으로 접근
'''

def explain(s):
    stack = []
    for case in s:
        if stack and stack[-1] == case: stack.pop()
        else: stack.append(case)
    return 0 if stack else 1