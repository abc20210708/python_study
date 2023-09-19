## 합분해 (골드 5)
#  참고 블로그 https://dreamtreeits.tistory.com/174

n, k = map(int, input().split())

dp = [[0] * (n + 1) for _ in range(k + 1)]
dp[0][0] = 1

for i in range(1, k + 1):
    for j in range(n + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000000

print(dp[k][n])

## dp[0][0] = 1에 대한 내 생각
#  dp[1][1] = 1이기 때문에 => dp[1][0]과 dp[0][0]은 1