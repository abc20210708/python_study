## 나선 (실버 4)

# 참고 블로그 https://blog.naver.com/charzim0611/222687769073
def solve_1941(n, m): # n 행, m이 열
    lst = [[0] * n for _ in range(m)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 오른쪽
    cur_x, cur_y = 0, 0
    num = 1
    idx = 0
    
    while True:
        if num == n*m:
            print(cur_y, cur_x)
            break
        
        lst[cur_x][cur_y] = 1
        now_x, now_y = cur_x + dx[idx], cur_y + dy[idx]
        
        if  0 <= now_x < m and 0 <= now_y < n and lst[now_x][now_y] == 0:
            cur_x, cur_y = now_x, now_y
            num += 1
        else:
            idx = (idx+1) % 4


# main
n, m = map(int, input().split())
solve_1941(n, m)


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