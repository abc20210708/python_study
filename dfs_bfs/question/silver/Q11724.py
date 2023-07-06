## 연결 요소의 개수 (실버 2)
# 참고 블로그 https://yuna0125.tistory.com/66

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# 정점의 개수 n과 간선의 개수 m 입력
n, m = map(int, input().split())

# 그래프 생성
graph = [[] for _ in range(n+1)]

# 간선 정보 입력받아 그래프에 추가
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 여부를 나타내는 리스트 초기화
visited = [0] * (n+1)

# 깊이 우선 탐색(DFS) 함수 정의
def dfs(v):
    visited[v] = 1  # 정점 v를 방문 처리
    for i in graph[v]:
        if visited[i] == 0:  # 방문하지 않은 인접 정점이 있다면
            dfs(i)  # 해당 정점으로 DFS 재귀 호출

# 연결 요소의 개수를 세는 변수 초기화
cnt = 0

# 모든 정점에 대해서 DFS 수행
for i in range(1, n+1):
    if visited[i] == 0:  # 방문하지 않은 정점이라면
        dfs(i)  # 해당 정점부터 DFS 수행
        cnt += 1  # DFS 수행 후에는 연결 요소 개수를 1 증가

print(cnt)  # 연결 요소의 개수 출력
            
                    