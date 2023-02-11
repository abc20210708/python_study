
# DFS 메서드 정의 다시 풀기
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드와 연결된 정보를 리스트 자료형으로 표현
# (2차원 리스트)    
graph = [
    [],
    [2, 3, 8], # 1
    [1, 7],    # 2
    [1, 4, 5], # 3
    [3, 5],    # 4
    [3, 4],    # 5
    [7],       # 6
    [2, 6, 8], # 7
    [1, 7]     # 8  
]       

# 각 노드가 바운된 정보를 리스트 자료형으로 표현
# (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
