## 연구소

## 참고 코드 https://www.acmicpc.net/source/67948636
# itertools 를 사용x, 조합으로
# 벽을 설치하고, 퍼져야함
# 일단 맵을 입력 받고, 벽을 설치할 수 있는 경우들에 대해서
# deepcopy한 후 설치

from copy import deepcopy
from collections import deque

n, m = map(int, input().split())

# 그래프를 입력 받으면서 조합할 빈칸들의 리스트를 만들어야한다.
virus_map = []
blank_point = []
virus_point = []

# bfs를 할 때 사용할 방향을 지정
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    line = list(map(int, input().split()))
    virus_map.append(line)
    for j in range(m):
        if line[j] == 0:
            blank_point.append((i, j))
        if line[j] == 2:
            virus_point.append((i, j))
            
def comb(arr, n):
    res = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        tmp = arr[i]
        for j in comb(arr[i+1:], n-1):
            res.append([tmp] + j)
    return res

# 조합 함수를 선언하고 설치 가능한 벽의 경우들을 후보 리스트로 만든다
cands =comb(blank_point, 3)

# bfs를 통해 바이러스를 확장시킨다. 이때, 각 후보들의 경우에 대해서
# virus_map이 바뀌지 않도록 deepcopy 이용

def bfs(graph):
    q = deque(virus_point)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx, ny))
    # bfs를 통해 바이러스로 감연시킨 후 안전구역의 값을 구한다.
    safe_zone = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                safe_zone += 1
    # 안전 구역의 값을 반환하고
    return safe_zone

answer = 0
for cand in cands:
    copy_map = deepcopy(virus_map)
    # 벽을 세우는 과정
    for point in cand:
        a, b = point
        copy_map[a][b] = 1
    # 벽을 세운 후 그래프에 bfs를 통해 safe_zone을 구한다
    answer = max(answer, bfs(copy_map))
    
print(answer)



'''
# 책
n, m = map(int, input().split())
data = [] # 초기 맵 리스트
tmp = [[0] * m for _ in range(n)] 

for _ in range(n):
    data.append(list(map(int, input().split())))
    
# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

res = 0

# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if tmp[nx][ny] == 0:
                # 해댱 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                tmp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기를 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매번 안적 영역의 크기 계산
def dfs(cnt):
    global res
    # 울타리가 3개 설치된 경우
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최댓값 계산
        res = max(res, get_score())
        return
    
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                cnt += 1
                dfs(cnt)
                data[i][j] = 0 
                cnt -= 1
                
dfs(0)
print(res)
'''