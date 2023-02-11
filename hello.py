
# 특정 거리의 도시 찾기 다시 풀기
from collections import deque

n, m, k, x = 4, 4, 2, 1

graph = [
         [],
         [2, 3],
         [3, 4],
         [],
         []
         ]

# 최단 거리 지정
distance = [-1] * (n + 1)
# 출발 지정
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for i in graph[now]:
        if distance[i] == -1:
            distance[i] = distance[now] + 1
            q.append(i)
            
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True
        
if check == False:
    print(-1)