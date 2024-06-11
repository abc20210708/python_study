## 유기농 배추 (실버 2) 
#  참고 블로그 https://moonsungo.tistory.com/entry/%EC%9D%8C%EB%A3%8C%EC%88%98-%EC%96%BC%EB%A0%A4%EB%A8%B9%EA%B8%B0%EC%99%80-%EC%9C%A0%EA%B8%B0%EB%86%8D-%EB%B0%B0%EC%B6%94%EB%B0%B1%EC%A4%80-1012-python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

t = int(input())
res = 0

def dfs(x, y):
    # 종료조건 1
    if x < 0 or x >= m or y < 0 or y >=n:
        return False
    
    # 성공조건
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True
    
    return False

for _ in range(t):    
    m, n, k = map(int, input().split())
    
    graph = [[0]*n for _ in range(m)]

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    for i in range(m):
        for j in range(n):
            if dfs(i, j):
                res += 1
                
    print(res)
    res = 0