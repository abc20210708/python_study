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
    
import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 우선순위, 값 형태
    distance[start] = 0
    
    while q:
        # 우선순위가 가장 낮은 값(가작 작은 거리)이 나온다
        dist, now = heapq.heappop(q)
        # 이미 입력 되어 있는 값이 현재 노드까지의 거리보다 작다면
        # 이미 방문한 노드이다. 따라서 다음으로 넘어감
        if distance[now] < dist:
            continue
        # 연결된 모든 노드 탐색
        for i in graph[now]:
            # 기존에 입력 되어 있는 값보다 크다면
            if dist+i[1] < distance[i[0]]:
                distance[i[0]] = dist+i[1]
                heapq.heappush(q, (dist+i[1], i[0]))
        

dijkstra(k)
print(distance)
