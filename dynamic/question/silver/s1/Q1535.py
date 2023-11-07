## 안녕 (실버 1)
#  참고 블로그 https://velog.io/@alsrl9165/%EB%B0%B1%EC%A4%80-1535%EB%B2%88-%EC%95%88%EB%85%95-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys
input = sys.stdin.readline

n = int(input())
L = [0] + list(map(int, input().split()))
H = [0] + list(map(int, input().split()))

dp = [[0]*101 for _ in range(n+1)]

for i in range(1, n+1):
    l, h = L[i], H[i]
    for j in range(1, 101):
        if j < l:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-l] + h)
            
print(dp[n][99])