'''
push X: 정수 X를 큐에 넣는 연산이다.

pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 
만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

size: 큐에 들어있는 정수의 개수를 출력한다.

empty: 큐가 비어있으면 1, 아니면 0을 출력한다.

front: 큐의 가장 앞에 있는 정수를 출력한다. 
만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

back: 큐의 가장 뒤에 있는 정수를 출력한다. 
만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다
'''

from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
queue = deque() 
   
for i in range(n):
    temp = input().split()
    
    if temp[0] == 'push':
        queue.insert(0, temp[1])
    elif temp[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif temp[0] == 'size':
        print(len(queue))
    elif temp[0] == 'empty':
        if len(queue) == 0 : print(1)
        else:
            print(0)
    elif temp[0] == 'front':
        if len(queue) == 0 : print(-1)
        else: print(queue[len(queue)-1])
    elif temp[0] == "back":
        if len(queue) == 0: print(-1)
        else: print(queue[0])