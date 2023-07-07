# 네트워크
## 참고 블로그 https://velog.io/@timointhebush/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-DFS-BFS-Python

# DFS 사용
def solution(n, computers):
    res = 0
    visited = [False] * n
    
    def dfs(computers, visited, v):
        visited[v] = True
        for i in range(n):
            # 현재 컴퓨터(v)와 연결된 컴퓨터(i)를 확인하고, 방문하지 않았다면 재귀적으로 방문
            if computers[v][i] == 1 and not visited[i]:
                dfs(computers, visited, i)
                
    for i in range(n):
        # 아직 방문하지 않은 컴퓨터라면, 네트워크의 개수를 증가시키고 DFS로 연결된 모든 컴퓨터 방문
        if not visited[i]:
            dfs(computers, visited, i)
            res += 1
            
    return res

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))
