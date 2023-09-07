## 나선 (실버 4)

## 참고 코드 https://www.acmicpc.net/source/64363047
from collections import deque

N, M = map(int, input().split())
w = deque(range(N))
h = deque(range(1, M))

x, y = 0, 0
left_right = 1
up_down = 1
while True:
    if w:
        if left_right == 1:
            x = w.pop()
        else:
            x = w.popleft()
        left_right *= -1
    else:
        break
    
    if h:
        if up_down == 1:
            y = h.pop()
        else:
            y = h.popleft()
        up_down *= -1
    else:
        break
print(x, y)