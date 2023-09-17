## 피보나치는 지겨웡~ (실버 3)
#  참고 블로그 https://nbalance97.tistory.com/96

n = int(input())
dp = [0] * (n+1)

if n <= 1:
    print(1)
else:
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2] + 1
    print(dp[n] % 1000000007)
