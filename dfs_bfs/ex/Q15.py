# 특정 거리의 도시 찾기

# 참고 블로그 https://soopeach.tistory.com/14

from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번화
n, m, k, x = map(int, input().split())

# 도시 1부터 확인하기 위해 그래프 0번째 칸은 빈칸으로 생성
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
# 예제 입력 1 기준 아래와 같이 그래프 생성
# [[], [2, 3],[3, 4],[],[]]
    
# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1) 
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            # 현재도시와 출발도시 사이의 거리 + 1
            distance[next_node] = distance[now] + 1
            q.append(next_node)
    
# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    # 도시들간에 최단 거리를 확인해
    # k와 동일하면 그 도시를 출력
    if distance[i] == k:
        print(i)
        # 최단 거리가 k인 도시가 존재한다면
        # True로 바꿔 -1이 출력되지 않도록
        check = True


# 만약 최단 거리가 k인 도시가 없다면, -1을 출력
if check == False:
    print(-1)
    