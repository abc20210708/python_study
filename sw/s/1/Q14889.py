## 스타트와 링크 (실버 1)
#  참고 블로그 https://zxl3651.tistory.com/56

import sys
input = sys.stdin.readline

def team(num, idx):
    # 현재 팀의 인원 수가 절반(n//2)이 되면
    if num == n//2:
        start_team, link_team = 0, 0
        # 팀의 능력치 계산
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:  # 둘 다 방문한 경우 스타트 팀
                    start_team += people[i][j]
                elif not visited[i] and not visited[j]:  # 둘 다 방문하지 않은 경우 링크 팀
                    link_team += people[i][j]
        # 스타트 팀과 링크 팀 능력치 차이를 리스트에 저장
        res.append(abs(start_team - link_team))
        return
    
    # 팀 구성하기
    for i in range(idx, n):
        if not visited[i]:  # 아직 방문하지 않은 사람만
            visited[i] = True  # 현재 사람을 방문 표시
            team(num+1, i+1)  # 다음 사람으로 재귀 호출
            visited[i] = False  # 재귀 호출 이후 방문 표시 해제
    
# 입력 부분
n = int(input())  # 총 사람 수 입력
people = [list(map(int, input().split())) for _ in range(n)]  # 능력치 정보 입력
res = []  # 결과를 저장할 리스트
visited = [False] * n  # 방문 표시 리스트 초기화
team(0, 0)  # 팀 구성 함수 호출
print(min(res))  # 결과 리스트 중 가장 작은 값 출력


# 참고 블로그 https://ryu-e.tistory.com/m/115
from itertools import combinations

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = int(1e9)

for comb in combinations(range(0, n), n//2):
    start = list(comb)
    link = [i for i in range(0, n) if i not in start]
    
    numS, numL = 0, 0
    
    for i in range(0, len(start)-1):
        for j in range(i+1, len(start)):
            numS += graph[start[i]][start[j]] + graph[start[j]][start[i]]
            numL += graph[link[i]][link[j]] + graph[link[j]][link[i]]
    ans = min(ans, abs(numS - numL))

print(ans)