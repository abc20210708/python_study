## A → B (실버 2)
#  참고 블로그 https://my-coding-notes.tistory.com/210

a, b = map(int, input().split())
tmp = 1

while b != a:
    tmp += 1
    num = b
    
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    
    if num == b:
        print(-1)
        break
else:
    print(tmp)
    

## BFS
from collections import deque
a, b = map(int, input().split())
q = deque()
q.append((a, 1))
tmp = 0

while q:
    x, y = q.popleft()
    
    if x > b:
        continue
    if x == b:
        print(y)
        break
    q.append((int(str(x)+"1"), y+1))
    q.append((x*2, y+1))
else:
    print(-1)    

        