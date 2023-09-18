## 동전 1 (골드 5)
#  참고 블로그 https://zu-techlog.tistory.com/48

n, k = map(int, input().split())

c = []
for _ in range(n):
    c.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1

for coin in c:
    for i in range(k+1):
        if i - coin >= 0:
            dp[i] += dp[i-coin]
            
print(dp[k])