# DFS 메서드 정의
def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)
            
# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)    
graph = [
    [],
    [2, 3, 8], # 1
    [1, 7],    # 2
    [1, 4, 5], # 3
    [3, 5],    # 4
    [3, 4],    # 5
    [7],       # 6
    [2, 6, 8,],# 7
    [1, 7]     # 8
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * len(graph)
# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

# DFS는 스택 자료구조에 기초한다.
# 실제로는 스택을 쓰지 않아도 되며 탐색을 수행함에 있어서
# 데이터의 개수가 N개인 경우 O(N)의 시간이 소요됩니다.
