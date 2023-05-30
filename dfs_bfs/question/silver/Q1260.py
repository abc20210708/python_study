## DFS와 BFS (실버 2) *
# 참고 블로그 https://velog.io/@hamfan524/%EB%B0%B1%EC%A4%80-1260%EB%B2%88-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC

from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    visted_lst1[v] = 1
    
    while q :
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if visted_lst1[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visted_lst1[i] = 1

def dfs(v):
    visted_lst2[v] = 1
    print(v, end=" ")
    for i in range(1, n+1):
        if visted_lst2[i] == 0 and graph[v][i] == 1:
            dfs(i)   
    

n, m, v = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
visted_lst1 = [0] * (n + 1)
visted_lst2 = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
    
dfs(v)
print()
bfs(v)