## 타일 장식물 (실버 5)

n = int(input())

dp = [0] + [1] * (n+3)

for i in range(2, n+3):
    dp[i] = dp[i-1] + dp[i-2]
    
print(dp[n]+dp[n+1]+dp[n+2])