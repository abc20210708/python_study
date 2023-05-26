## 달팽이 (실버 3) *
# 참고 블로그 https://devlibrary00108.tistory.com/259

import sys
input = sys.stdin.readline

def make_snail(n):
    global tx,ty
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    arr = [[0] * n for _ in range(n)]
    
    # 0,0 에서 초기화
    cnt = n ** 2
    direction = 0
    x, y = 0, 0
    arr[x][y] = cnt
    cnt -= 1
    # cnt 가 모든 칸에 기록될때까지
    while cnt > 0:

        nx = x + dx[direction]
        ny = y + dy[direction]

        if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
            arr[nx][ny] = cnt
            if cnt==target:
                tx,ty = nx,ny
            x, y = nx, ny
            cnt -= 1
        else:       # 진입 못하면 방향 시계방향 전환
            direction = (direction+1) % 4
    return arr


N = int(input())
target = int(input())
tx, ty = 0, 0
snail = make_snail(N)

for row in snail:
    print(*row)
print(tx+1, ty+1)