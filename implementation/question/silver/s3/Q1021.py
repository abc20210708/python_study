## 회전하는 큐 (실버 3)
#  참고 블로그 https://archive-me-0329.tistory.com/11
from sys import stdin
from collections import deque

def firstFun():
    q.popleft()

def secondFun(second):
    q.append(q.popleft())
    return second + 1

def thirdFun(third):
    q.appendleft(q.pop())
    return third + 1


q = deque()
N, M = map(int, stdin.readline().split())
pick = list(map(int, stdin.readline().split()))
for i in range(1,N+1): q.append(i)

second = 0
third = 0

for num in pick:
    while num != q[0]:
        if q.index(num) <= len(q)//2:
            second = secondFun(second)
        elif q.index(num) > len(q)//2:
            third = thirdFun(third)
    if num == q[0]: firstFun()

print(second + third)