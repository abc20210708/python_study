
# BFS 예제 다시 풀기

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은
        # 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    


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
bfs(graph, 1, visited)
