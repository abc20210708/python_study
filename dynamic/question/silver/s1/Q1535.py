## 안녕 (실버 1)
#  참고 블로그 https://tooo1.tistory.com/542
import sys
input = sys.stdin.readline

n = int(input())
l_lst = [0] + list(map(int, input().split()))
j_lst = [0] + list(map(int, input().split()))

dp = [[0 for _ in range(101)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 101):
        if l_lst[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-l_lst[i]] + j_lst[i])
        else:
            dp[i][j] = dp[i-1][j]
            
print(dp[n][99])

