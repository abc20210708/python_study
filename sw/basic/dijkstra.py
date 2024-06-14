## 다익스트라 
#  참고 블로그 https://velog.io/@tks7205/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-with-python

n, m = map(int, input().split())
k = int(input()) # 시작할 노드
INF = 1e8

graph = [[] for _ in range(n+1)] # 1번 노드부터 시작, +1

visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    # u: 출발노드, v:도착노드, w: 연결된 간선의 가중치
    u, v, w = map(int, input().split()) 
    graph[u].append((v, w))
    
def get_small_node():
    min_val = INF
    idx = 0
    for i in range(1, n+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            idx = i
    return idx

def dijkstra(start):
    distance[start] = 0 # 시작 노드는 0으로 초기화
    visited[start] = True
    
    for i in graph[start]:
        distance[i[0]] = i[1] # 시작 노드와 연결된 노드들의 거리 입력
        
    for _ in range(n-1):
        # 거리가 구해진 노드 중 가장 잛은 거리인 것을 선택
        now = get_small_node() 
        visited[now] = True # 방문 처리
        
        for j in graph[now]:
            # 기존에 입력된 값보다 더 작은 거리가 나온다면
            if distance[now] + j[1] < distance[j[0]]:
                distance[j[0]] = distance[now] + j[1]
                
dijkstra(k)
print(distance)
