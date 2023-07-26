## 이동하기 (실버 2)
#  참고 블로그 https://velog.io/@sugenius77/백준Python-11048번-이동하기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[0] * (m+1)]

for _ in range(n):
    graph.append([0]+list(map(int, input().split())))
    
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = graph[i][j] + max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        
print(dp[n][m])