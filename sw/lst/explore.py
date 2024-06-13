## 고대 문명 유적 탐사

from collections import deque

# K: 최대 회전 횟수, M: 사용할 수의 개수
K, M = map(int, input().split())

# 5x5 유적지 배열을 입력받음
arr = [list(map(int, input().split())) for _ in range(5)]

# 사용할 숫자들을 입력받음
numbers = list(map(int, input().split()))

# 네 방향 이동을 위한 좌표 설정 (하, 우, 상, 좌)
dire = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# BFS 탐색 함수
def bfs(x, y, n):
    connected = [(x, y)]
    q = deque([(x, y)])
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in dire:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and not V[ny][nx] and arr[ny][nx] == n:
                q.append((nx, ny))
                connected.append((nx, ny))
                V[ny][nx] = True
                cnt += 1
    return cnt, connected

# 중심 좌표를 기준으로 주변 8칸의 값을 읽어오는 함수
def read_pivot(px, py):
    Q, I = deque(), deque()
    for x, y in [(px-1, py-1), (px, py-1), (px+1, py-1), (px+1, py), (px+1, py+1), (px, py+1), (px-1, py+1), (px-1, py)]:
        Q.append(arr[y][x])
        I.append((x, y))
    return Q, I

# 회전 후 배열을 업데이트하는 함수
def update():
    for i in range(8):
        x, y = I[i]
        arr[y][x] = Q[i]

# 점수를 계산하는 함수
def get_score():
    score = 0
    for y in range(5):
        for x in range(5):
            if not V[y][x]:
                V[y][x] = True
                size, connected = bfs(x, y, arr[y][x])
                if size >= 3:
                    score += size
    return (score, angle, px, py)

use = 0

# 최대 K번의 회전 실행
for _ in range(K):
    answer = 0
    scores = []
    for py in range(1, 4):
        for px in range(1, 4):
            Q, I = read_pivot(px, py)
            for angle in (90, 180, 270):
                V = [[False] * 5 for _ in range(5)]
                Q.rotate(2)
                update()
                scores.append(get_score())
            Q.rotate(2)
            update()
            
    scores.sort(key=lambda x: (-x[0], x[1], x[2], x[3]))
    score, angle, ax, ay = scores[0]
    
    if not score:
        break

    # 최고 점수인 경우로 회전
    Q, I = read_pivot(ax, ay)
    Q.rotate(2 * (angle // 90))
    update()

    while True:
        score = 0
        V = [[False] * 5 for _ in range(5)]
        for y in range(5):
            for x in range(5):
                if not V[y][x]:
                    V[y][x] = True
                    size, info = bfs(x, y, arr[y][x])
                    if size >= 3:
                        score += size
                        for zx, zy in info:
                            arr[zy][zx] = 0
        if not score:
            break
        
        answer += score
        for j in range(5):
            for i in range(4, -1, -1):
                if arr[i][j] == 0:
                    arr[i][j] = numbers[use]
                    use += 1

    print(answer, end=' ')
