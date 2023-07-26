## 오르막 수 (실버 1)

## 참고 블로그 https://great-park.tistory.com/98

import sys
input = sys.stdin.readline

n = int(input())

dp = [[0 for i in range(10)] for j in range(n+1)]

# 1의 자릿수 초기화
for x in range(10):
    dp[1][x] = 1
    
for i in range(2, n+1): # i번째 자릿수
    for k in range(10): # 0-9
        tmp = 0
        for s in range(0, k+1): # i-1자리 수에서 0-k까지 더하기
            tmp += dp[i-1][s]
        dp[i][k] = tmp

res = 0
for i in range(10):
    res += dp[n][i]
print(res % 10007)