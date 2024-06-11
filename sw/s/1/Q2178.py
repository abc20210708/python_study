## 미로 탐색 (실버 1)
## 미로 탐색 (실버 1)
import sys
input = sys.stdin.readline
from collections import deque

def BFS(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간을 벗어난 경우는 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우만 최단 거리를 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] +1
                q.append((nx, ny))
    return graph[n-1][m-1]



n, m = map(int, input().split())

graph = []

for _ in range(n):
    tmp = input().rstrip()
    tmp = list(map(int, tmp))
    graph.append(tmp)
    
# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(BFS(0, 0))