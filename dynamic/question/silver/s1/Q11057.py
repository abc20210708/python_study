## 오르막 수 (실버 1)

## 참고 블로그 https://great-park.tistory.com/98

import sys
input = sys.stdin.readline

n = int(input())

dp = [[0 for i in range(10)] for j in range(n+1)]

# 1의 자릿수 초기화
for x in range(10):
    dp[1][x] = 1
    

for i in range(2, n+1):  # 길이가 2부터 n까지의 오르막 수 개수를 계산합니다.
    for k in range(10):  # k는 마지막 자리 숫자를 의미합니다. (0부터 9까지)
        tmp = 0
        for s in range(0, k+1):  #i-1자리 수에서 0-k까지 더하기 / 마지막 자리 숫자보다 작거나 같은 숫자들을 모두 더합니다. 
            tmp += dp[i-1][s]
        dp[i][k] = tmp  # 현재 길이와 마지막 자리 숫자에 해당하는 오르막 수 개수를 저장합니다.

res = 0
for i in range(10):
    res += dp[n][i]
print(res % 10007)