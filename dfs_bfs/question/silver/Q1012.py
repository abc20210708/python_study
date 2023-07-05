## 유기농 배추 (실버 2) *
# 참고 블로그 https://hongcoding.tistory.com/72
from collections import deque

dx = [-1 ,1 ,0, 0]  # 상하좌우로 이동하기 위한 x좌표 변화량
dy = [0, 0, -1, 1]  # 상하좌우로 이동하기 위한 y좌표 변화량

t = int(input())  # 테스트 케이스의 개수 입력

def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0  # 현재 위치를 방문했음을 표시하기 위해 0으로 변경

    while queue:
        x, y = queue.popleft()
        for i in range(4):  # 상하좌우로 이동
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:  # 그래프 범위를 벗어나는 경우 무시
                continue
            if graph[nx][ny] == 1:  # 인접한 배추가 있는 경우
                graph[nx][ny] = 0  # 인접한 배추를 방문했음을 표시하기 위해 0으로 변경
                queue.append((nx, ny))  # 인접한 배추의 위치를 큐에 추가
    return

for i in range(t):
    cnt = 0
    n, m, k = map(int,input().split())  # 배추밭의 가로, 세로 길이와 배추의 개수 입력
    graph = [[0] * m for _ in range(n)]  # 배추밭 초기화

    for j in range(k):
        x, y = map(int, input().split())  # 배추의 위치 입력
        graph[x][y] = 1  # 배추가 있는 위치를 1로 표시

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:  # 아직 방문하지 않은 배추가 있는 경우
                bfs(graph, a, b)  # 해당 배추와 연결된 모든 배추 방문
                cnt += 1  # 배추흰지렁이가 필요한 지역 개수 증가
    print(cnt) 