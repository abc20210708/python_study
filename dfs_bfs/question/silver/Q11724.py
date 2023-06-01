## 연결 요소의 개수 (실버 2)
# 참고 블로그 https://yuna0125.tistory.com/66

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]



for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [0] * (n+1)
def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)


cnt = 0

for i in range(1, n+1):
        if visited[i] == 0:
            dfs(i)
            cnt += 1
                
print(cnt)
            
                    