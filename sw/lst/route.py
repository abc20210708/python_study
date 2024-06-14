## 보급로
#  참고 블로그 https://glory-summer.tistory.com/181

from collections import deque

def dijkstra(x, y):
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = deque([(x, y)])
    dp[x][y] = 0
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in dxy:
            nx, ny = x+dx , y+dy
            
            if 0 <= nx < n and 0<= ny < n:
                if dp[nx][ny] > dp[x][y] + graph[nx][ny]:
                    q.append((nx, ny))
                    dp[nx][ny] = dp[x][y] + graph[nx][ny]


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    graph = [list(map(int, list(input()))) for _ in range(n)]
    dp = [[float('inf') for _ in range(n)] for _ in range(n)]
    dijkstra(0, 0)
    print(f"#{tc} {dp[n-1][n-1]}")

