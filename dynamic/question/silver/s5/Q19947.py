## 투자의 귀재 배주형 (실버 5)
#  참고 블로그 https://tw0226.tistory.com/50

h, y = map(int, input().split())

dp = [0] * (y+1)
dp[0] = h

for i in range(1, y+1):
    if i >= 5:
        dp[i] = max(dp[i-1]*1.05, dp[i-3]*1.2, dp[i-5]*1.35)
    elif i >= 3:
        dp[i] = max(dp[i-1]*1.05, dp[i-3]*1.2)
    else:
        dp[i] = dp[i-1] * 1.05
    dp[i] = int(dp[i])

print(int(dp[y]))