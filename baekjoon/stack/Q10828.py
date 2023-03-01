'''
push X: 정수 X를 스택에 넣는 연산이다.

pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

size: 스택에 들어있는 정수의 개수를 출력한다.

empty: 스택이 비어있으면 1, 아니면 0을 출력한다.

top: 스택의 가장 위에 있는 정수를 출력한다. 
만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

참고 블로그
https://velog.io/@wjdtmdgml/%EB%B0%B1%EC%A4%80%EC%8A%A4%ED%83%9D10828%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0%EC%8A%A4%ED%83%9D
'''
import sys

stack = []
input = sys.stdin.readline
n = int(input())

for i in range(n):
    temp = input().split()
    
    if temp[0] == 'push':
        stack.append(temp[1])
    elif temp[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif temp[0] == 'size':
        print(len(stack))
    elif temp[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif temp[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    # 스택에서 원소를 제거하지 않고 가져오기만 할 때에는
    # [-1]을 이용하여 찾을 수 있습니다.