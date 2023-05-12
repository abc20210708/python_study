## 바이러스 (실버 3) *
# 참고 코드 https://www.acmicpc.net/source/54241783

import sys
input = sys.stdin.readline

n = int(input())  
m = int(input()) 

# 방문 여부를 저장할 리스트 초기화
visited = [0] * (n + 1)  

# 컴퓨터 간의 연결 정보를 저장할 그래프 초기화
graph = [[] for _ in range(n+1)]  
for _ in range(m):
    # 연결된 컴퓨터 쌍 입력
    a, b = map(int, input().split())  
    # a와 b가 연결되어 있다는 정보를 그래프에 저장
    graph[a].append(b) 
    # b와 a가 연결되어 있다는 정보도 그래프에 저장 (양방향)
    graph[b].append(a)  

cnt = 0  # 감염된 컴퓨터 수를 세는 변수 초기화

def dfs(v):  # 깊이 우선 탐색 함수
    visited[v] = 1  # 현재 컴퓨터를 방문 처리
    global cnt  # cnt 변수를 전역 변수로 사용하기 위해 global 선언

    for i in graph[v]:  # 현재 컴퓨터와 연결된 컴퓨터들을 하나씩 탐색
        if visited[i] == 0:  # 아직 방문하지 않은 컴퓨터라면
            dfs(i)  # 해당 컴퓨터를 방문하고, 재귀적으로 dfs 호출
            cnt += 1  # 방문한 컴퓨터의 수를 1 증가시킴

dfs(1)  # 1번 컴퓨터부터 시작하여 감염된 컴퓨터 수를 구함
print(cnt)  # 결과 출력
