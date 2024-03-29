## 연구소

# 세로 n, 가로 m
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