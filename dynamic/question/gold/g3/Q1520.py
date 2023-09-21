## 내리막 길 (골드 3)
#  참고 블로그 https://hye-z.tistory.com/48

import sys
sys.setrecursionlimit(10**7)

m, n = map(int, input().split()) # h: 세로, w: 가로
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

vst = [[-1] * n for _ in range(m)]

def dfs(x, y): # x: row, y: col
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    # 도착 지검에 도달하면 1(한 가지 경우의 수)를 리턴
    if x == (m-1) and y == (n-1):
        return 1
    
    if vst[x][y] != -1:
        return vst[x][y]
    
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 탐색 범위를 벗어나는 경우 pass
        if nx < 0 or ny < 0 or nx > (m-1) or ny > (n-1):
            continue
        # 내리막 일 경우 (현재 길 < 이전 길)
        if arr[nx][ny] < arr[x][y]:
            cnt += dfs(nx, ny)
    
    vst[x][y] = cnt
    return vst[x][y]

print(dfs(0, 0))