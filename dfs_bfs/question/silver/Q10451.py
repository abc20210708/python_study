## 순열 사이클 (실버 3)
#  참고 블로그 https://claude-u.tistory.com/434

import sys
sys.setrecursionlimit(2000)

def dfs(x):
    visited[x] = True # 방문 체크
    num = nums[x] # 다음 방문 장소
    if not visited[num]: # 방문하지 않았다면
        dfs(num) # 재귀
    
for _ in range(int(input())):
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    visited = [True] + [False] * n #방문 여부 확인용
    res = 0
    
    for i in range(1, n+1):
        if not visited[i]: # 방문하지 않았다면
            dfs(i) # dfs 실행
            res += 1
    print(res)
            