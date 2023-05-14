## 점프 점프 (실버 2) *
# 참고 블로그 https://jinho-study.tistory.com/918
from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    chk[x] = 1
    while q:
        x = q.popleft()
        for i in [-graph[x], graph[x]]:
            tmp = x + i
            if (0 <= tmp < n) and chk[tmp] == 0:
                q.append(tmp)
                chk[tmp] = 1

n = int(input())
graph = list(map(int, input().split()))
# 시작점
k = int(input())-1
chk = [0] * n
bfs(k)
print(chk.count(1)) 

