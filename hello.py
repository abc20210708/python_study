
# 장애물 인식 프로그램 다시 풀기

import sys

def dfs(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= n:
        return False
    # 노드를 방문하지 않았다면
    if block[x][y] == 1:
        cnt.append(1)
        
        block[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


# 지도의 크기 N
n = 7

block = [
    [1,1,1,0,1,1,1],
    [0,1,1,0,1,0,1],
    [0,1,1,0,1,0,1],
    [0,0,0,0,1,0,0],
    [0,1,1,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,1,1,0,0,0,0],
    ]
# 자료 입력
#for i in range(n):
#   block.append(list(map(int, input())))

result = 0
cnt = []
result_list = []
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1
            result_list.append(len(cnt))
            cnt = []

print(result)
result_list.sort()
for i in result_list:
    print(i)