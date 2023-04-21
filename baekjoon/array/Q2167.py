## 2차원 배열의 합 (실버 5) *

# 참고 블로그 https://blog.naver.com/parkjh9876/221867004374
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
Q = [tuple(map(int, input().split())) for _ in range(K)]
dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + A[i - 1][j - 1]

for i in Q:
    (x1, y1, x2, y2) = i
    result = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    print(result)