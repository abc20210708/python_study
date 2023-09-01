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

'''
예제 1번 95,229을 예로 들면
만약 3년마다를 계산해보면
95,229 + (95,229 * 0.2)
더 간략하게 계산
95,229 * 1.2
'''