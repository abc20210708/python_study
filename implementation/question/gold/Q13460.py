## 구슬 탈출 2 (골드 1) *
# 참고 블로그 https://lottegiantsv3.tistory.com/52
from collections import deque
import sys


n, m = map(int, input().split())


graph = []
R = [0, 0]
B = [0, 0]
target = [0, 0]
for a in range(n):
    sub = list(input())
    graph.append(sub)
    for b in range(m):
        if sub[b] == 'R':
            R = [a, b]
        elif sub[b] == 'B':
            B = [a, b]
        elif sub[b] == 'O':
            target = [a, b]

chk = False

# 상, 하, 좌, 우
dx = [0,1,0,-1]
dy = [1,0,-1,0]

q = deque()

# R 좌표, B 좌표
q.append((R[0], R[1], B[0], B[1], 0))

visited = set()
visited.add((R[0], R[1], B[0], B[1]))

while q:
    rx, ry, bx, by, cnt = q.popleft()

    if graph[rx][ry] == 'O':
        print(cnt)
        chk = True
        break


    if cnt >= 10:
        continue


    # r, b 움직이기
    for k in range(4):
        r_move = 0
        b_move = 0

        # r 움직이기
        nrx = rx + dx[k]
        nry = ry + dy[k]

        while 1:
            if graph[nrx][nry] == '#':
                nrx -= dx[k]
                nry -= dy[k]
                break
            elif graph[nrx][nry] == 'O':
                break

            nrx += dx[k]
            nry += dy[k]

            r_move += 1
        # b 움직이기
        nbx = bx + dx[k]
        nby = by + dy[k]
        while 1:
            if graph[nbx][nby] == '#':
                nbx -= dx[k]
                nby -= dy[k]
                break
            elif graph[nbx][nby] == 'O':
                break
            nbx += dx[k]
            nby += dy[k]
            b_move += 1

        # B 빠지면 안됨
        if graph[nbx][nby] == 'O':
            continue

        # r, b가 같은 경우 / O일때 아닐때
        if nrx == nbx and nry == nby:

            if r_move > b_move:
                nrx -= dx[k]
                nry -= dy[k]
            else:
                nbx -= dx[k]
                nby -= dy[k]

        if not (nrx, nry, nbx, nby) in visited:
            visited.add((nrx, nry, nbx, nby))
            q.append((nrx, nry, nbx, nby, cnt+1))


if chk == False:
    print(-1)