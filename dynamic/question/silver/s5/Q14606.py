## 피자 small (실버 5)
#  참고 블로그 https://jinho-study.tistory.com/971

dp = [0]*(11)
dp[1] = 0
dp[2] = 1
for i in range(3, N+1):
    m = i//2
    dp[i] = m*(i-m) + dp[m] + dp[i-m]
print(dp[N])