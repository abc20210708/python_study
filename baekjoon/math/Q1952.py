## 달팽이2 (브론즈 1) *

dx = [0, 1, 0, -1]  # 달팽이가 이동할 수 있는 방향 (우, 하, 좌, 상)
dy = [1, 0, -1, 0]

m, n = map(int, input().split())  # m: 세로 길이, n: 가로 길이

# m x n 크기의 2차원 배열을 생성하고, 초기값을 -1로 설정
g = [[-1] * n for _ in range(m)]

x = y = 0  # 시작 위치 (좌측 상단)
g[x][y] = 0  # 시작 위치의 값을 0으로 설정
cnt = 0  # 몇 바퀴를 돌았는지 카운트하는 변수
d = 0  # 현재 이동 방향 (우측)

while True:
    changed = False  # 방향을 전환하는지 여부를 저장하는 변수
    go = False  # 이동 가능한지 여부를 저장하는 변수
    for i in range(d, d+4):  # 현재 방향부터 시계방향으로 탐색
        nx, ny = x + dx[i%4], y + dy[i%4]  # 이동할 위치 계산
        # 이동할 위치가 배열 범위를 벗어나거나 이미 방문한 적이 있으면 스킵
        if nx < 0 or ny < 0 or nx >= m or ny >= n or g[nx][ny] != -1:
            changed = True
            continue
        go = True
        g[nx][ny] = 0  # 이동할 위치를 방문했다고 표시
        x, y, d = nx, ny, i%4  # 위치와 방향을 업데이트
        break
    # 현재 방향에서 이동 가능한 위치가 없다면 반복문을 종료
    if changed == True and go == True:
        cnt += 1  # 방향을 전환했으므로 바퀴 수를 증가
    if go == False:
        break
    
print(cnt)  # 바퀴 수 출력
