## 뱀 (골드 4) **
# 참고 블로그 https://velog.io/@daeungdaeung/%EB%B0%B1%EC%A4%80-3190-%EB%B1%80with-Python

import sys
from collections import deque

N = int(input())
K = int(input())

# 맵(brd)에 사과 표시
brd = [[0] * N for _ in range(N)]
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    brd[r-1][c-1] = 2

# 뱀의 이동 정보 저장
L = int(input())
snake_directions = deque([])
for _ in range(L):
    sec, d = sys.stdin.readline().split()
    snake_directions.append([int(sec), d])

NESW = [[-1, 0],[0, 1],[1, 0],[0, -1]]

r, c = 0, 0
brd[r][c] = 1
snake = deque([[r, c]])
d = 1
t = 0
flag = False

while True:
    # 조건 1. 이번에 뱀의 방향을 바꿔야하는 정보가 존재 
    # 조건 2. 뱀의 방향을 바꿔야하는 경우
    if len(snake_directions) and snake_directions[0][0] == t:
        _, tmp_d = snake_directions.popleft()
        if tmp_d == 'D':
            d = (d + 1) % 4
        else:
            d = (d + 3) % 4

    r, c = snake[0]
    dr, dc = NESW[d]
    if 0 <= r + dr < N and 0 <= c + dc < N:
        # 사과 먹은 경우
        if brd[r + dr][c + dc] == 2:
            snake.appendleft([r + dr, c + dc])
            brd[r + dr][c + dc] = 1
        else:
            # 자기 몸통을 물어버린 경우...
            if brd[r + dr][c + dc] == 1:
                flag = True
                pass
            else:
                # 꼬리가 다음 칸으로 옮겨질거라 빼버림
                tail_r, tail_c = snake.pop()
                # 맵에 해당 정보 기입
                brd[tail_r][tail_c] = 0
                # 머리가 움직였으니 appendleft로 머리 저장
                snake.appendleft([r + dr, c + dc])
                # 당연히 이것도 맵에 정보 기입
                brd[r + dr][c + dc] = 1
    # 벽에 부딪힌 경우
    else:
        flag = True
    t += 1

    if flag:
        break

print(t)