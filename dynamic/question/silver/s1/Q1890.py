## 점프 (실버 1)
#  참고 블로그 https://dreamtreeits.tistory.com/212

import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n -1 and j == n - 1:
            print(dp[i][j])
            break
        tmp = lst[i][j] 
        
        if j + tmp < n:
            dp[i][j+tmp] += dp[i][j]
        if i + tmp < n:
            dp[i+tmp][j] += dp[i][j]