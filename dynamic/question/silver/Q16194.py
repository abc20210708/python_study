## 카드 구매하기 2 (실버 1) *
'''
n = int(input())
price = [0] + list(map(int, input().split()))
d = [9999999999] * (n+1)
d[0] = 0

for i in range(n+1):
    for k in range(i+1):
        d[i] = min(d[i], d[i-k] + price[k])

print(d[n])
'''

## 다른 풀이
# 찹고 블로그 https://velog.io/@y7y1h13/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EB%B0%B1%EC%A4%80-16194-%EC%B9%B4%EB%93%9C-%EA%B5%AC%EB%A7%A4%ED%95%98%EA%B8%B0-2python
from copy import deepcopy

N = int(input())
a = [0] + list(map(int, input().split()))
dp = deepcopy(a)
for i in range(1, N + 1):
    for k in range(1, i + 1):
        dp[i] = min(dp[i], dp[i - k] + a[k])
        print(f"dp[i] = {dp[i]}")
        print(f"dp[i-k]+a[k] = {dp[i-k]+a[k]}")
print(dp[N])