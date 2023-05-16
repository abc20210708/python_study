## 점프 점프 (실버 2) *
# 참고 블로그 https://jinho-study.tistory.com/918
from collections import deque

def bfs(x):
    q = deque()
    # 시작점을 큐에 추가
    q.append(x)  
    # 시작점을 방문했음을 표시
    chk[x] = 1  
    while q:
        x = q.popleft()  # 큐에서 원소를 하나 꺼냅니다.
        # 현재 위치에서 앞으로 이동하는 경우와 뒤로 이동하는 경우를 고려
        for i in [-graph[x], graph[x]]:  
            tmp = x + i  # 이동한 위치를 계산합니다.
            # 이동한 위치가 범위 내에 있고 아직 방문하지 않은 곳이라면
            if (0 <= tmp < n) and chk[tmp] == 0:  
                q.append(tmp)  # 큐에 추가
                chk[tmp] = 1  # 이동한 위치를 방문했음을 표시

n = int(input())  
graph = list(map(int, input().split())) 
# 시작점을 입력받습니다. (인덱스는 0부터 시작하므로 1을 뺍니다.)
k = int(input())-1 
chk = [0] * n  # 돌을 방문한 여부를 저장하는 리스트를 초기화
bfs(k)  # bfs 함수를 호출하여 시작점부터 탐색을 시작
#print(chk.count(1))  # 방문한 돌의 개수를 출력
print(sum(chk))


# 다른 풀이
# 참고 블로그 https://yeoooo.github.io/algorithm/BOJ14248/
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input().rstrip())
v = [0]*(n+1)
bridge = list(map(int, input().split()))
s = int(input().rstrip())
cnt = 1
def dfs(x):
    global cnt
    for i in range(2):
        if not i:
            nx = x+bridge[x]
        else:
            nx = x-bridge[x]
        if 0<=nx<n and not v[nx]:
            v[nx] = 1
            cnt += 1
            dfs(nx)
dfs(s-1)
print(cnt)

