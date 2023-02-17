# 장애물 인식 프로그램

import sys

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        # 장애물의 개수 체크
        cnt.append(1)
        # 해당 노드 방문 처리
        graph[x][y] = 0
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


# 지도 크기를 입력받는다.
#n = int(sys.stdin.readline())
n = 7
cnt = []
# 2차원 리스트의 맵 정보 입력 받는다.
graph = [
    [1,1,1,0,1,1,1],
    [0,1,1,0,1,0,1],
    [0,1,1,0,1,0,1],
    [0,0,0,0,1,0,0],
    [0,1,1,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,1,1,0,0,0,0],
    ]
#for i in range(n):
#    graph.append(list(map(int, input().strip())))

'''
lstrip()은 문자열에서 왼쪽 공백을 모두 삭제하고, 
rstrip()은 오른쪽 공백을 모두 삭제합니다. 
strip()은 양쪽 공백을 모두 삭제합니다.
'''

# 모든 노드(위치)에 대하여 장애물 블록을 만든다.
result = 0
result_list = []
for i in range(n):
    for j in range(n):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1
            # 길이를 통해 장애물의 개수 확인
            result_list.append(len(cnt))
            cnt = []

# 총 블록의 수 출력
print(result)
# 장애물의 수 오름차순 정렬 후 출력
result_list.sort()
for i in result_list:
    print(i)