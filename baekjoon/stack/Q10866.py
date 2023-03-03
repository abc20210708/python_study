# deque

from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
d = deque() 
   
for i in range(n):
    temp = input().split()
    
    if temp[0] == 'push_front':
        d.appendleft(temp[1]) # 앞에 넣는다
    elif temp[0] == 'push_back':
        d.append(temp[1])     # 뒤에 넣는다.
    elif temp[0] == 'pop_front': # 가장 앞에 있는 수를 빼고 출력
        if d:
            print(d[0])
            d.popleft()
        else:
            print(-1)
    elif temp[0] == 'pop_back': # 가장 뒤에 있는 수를 빼고 출력
        if d: 
            print(d[len(d)-1])
            d.pop()
        else: print(-1)
    elif temp[0] == 'size':
        print(len(d))
    elif temp[0] == 'empty':
        if d : print(0)
        else:
            print(1)
    elif temp[0] == 'front':
        if d: print(d[0])
        else: print(-1)
    elif temp[0] == "back":
        if d: print(d[len(d)-1])
        else: print(-1)