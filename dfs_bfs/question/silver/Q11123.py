## 양 한마리... 양 두마리... (실버 2) *
# 참고 블로그 https://seokii.tistory.com/m/101

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(x, y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False
    if graph[x][y] == "#":
        graph[x][y] = "."

        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        
        return True
    return False

t = int(input())

for _ in range(t):
    h, w = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            # 양이 발견된 경우
            if graph[i][j] == "#":
                if dfs(i, j):
                    cnt += 1
    print(cnt)       
    