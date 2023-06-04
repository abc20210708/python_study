## 극장 좌석 (실버 1) *
# 참고 블로그 https://codedrive.tistory.com/432
# https://parase.tistory.com/9

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())


if n >= 2:
    dp = [1] * (n + 1)
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]
    start = 1
    res = 1
    for _ in range(m):
        vip = int(input())
        res *= dp[vip - start]
        start = vip + 1
    print(res * dp[n - start + 1])
else:
    for _ in range(m):
        vip = int(input())
    print(1)

