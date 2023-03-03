'''
큐

push X: 정수 X를 큐에 넣는 연산이다.

pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 
만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

size: 큐에 들어있는 정수의 개수를 출력한다.

empty: 큐가 비어있으면 1, 아니면 0을 출력한다.

front: 큐의 가장 앞에 있는 정수를 출력한다. 
만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

back: 큐의 가장 뒤에 있는 정수를 출력한다. 
만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다

참고 블로그
https://velog.io/@deannn/BOJ-%EB%B0%B1%EC%A4%80-10845%EB%B2%88-%ED%81%90-Python

'''

import sys

input = sys.stdin.readline

n = int(input())

d = list()

for _ in range(n):
    temp = input().split()
    
    if temp[0] == "push":
        d.append(int(temp[1]))
    elif temp[0] == "pop":
        if d: print(d.pop(0))
        else: print(-1)
    elif temp[0] == "size":
        print(len(d))
    elif temp[0] == "empty":
        if d: print(0)
        else : print(1)
    elif temp[0] == "front":
        if d: print(d[0])
        else: print(-1)
    elif temp[0] == "back":
        if d: print(d[-1])
        else: print(-1)
    

'''
queue = list() 
   
for i in range(n):
    temp = input().split()
    
    if temp[0] == 'push':
        queue.append(int(temp[1]))
    elif temp[0] == 'pop':
        if not queue : print(-1) # queue가 빈 경우
        else : print(queue.pop(0))
    elif temp[0] == 'size':
        print(len(queue))
    elif temp[0] == 'empty':
        if not queue : print(1)
        else : print(0)
    elif temp[0] == 'front':
        if not queue : print(-1)
        else: print(queue[0])
    elif temp[0] == "back":
        if not queue: print(-1)
        else: print(queue[-1])
'''