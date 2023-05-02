## AC (골드 5)*

# 참고 블로그 https://clap0107.tistory.com/16

from collections import deque
import sys

t = int(input())

for _ in range(t):
    p = sys.stdin.readline().strip()
    n = int(input())
    nums = input()[1:-1].split(',')
    p = p.place("RR", "")

    queue = deque(nums)

    reverse = 0
    flag = False

    if n == 0:
        queue = []

    for i in p:
        if i == 'R':
            reverse += 1
        else:
            if len(queue) == 0:
                print('error')
                flag = True
                break
            elif reverse % 2 == 1:
                queue.pop()
            else:
                queue.popleft()

    if not flag:
        if reverse % 2 == 1:
            queue.reverse()
        print('[' + ','.join(queue) + ']')
                
    