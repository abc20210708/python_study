## 상근이의 여행 (실버 4)
#  참고 블로그 https://jinho-study.tistory.com/889
import sys
input = sys.stdin.readline

def dfs(idx, cnt):
    
    chk[idx] = 1
    
    for n in graph[idx]:
        if chk[n] == 0:
            cnt = dfs(n, cnt+1)
    return cnt

for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    chk = [0] * (n+1)
    cnt = dfs(1, 0)
    print(cnt)



#  참고 블로그 https://harang1412.tistory.com/744




for _ in range(int(input())):
    n, m = map(int, input().split())
    for i in range(m):
        a, b = map(int, input().split())
    print(n-1)