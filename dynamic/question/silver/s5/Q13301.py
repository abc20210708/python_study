## 타일 장식물 (실버 5)

n = int(input())

dp = [0] + [1] * (n+2)

for i in range(2, n+3):
    dp[i] = dp[i-1] + dp[i-2]
    
print(dp[n]+dp[n+1]+dp[n+2])

'''

 dp = [0, 1, 1, 2, 3, 5, 8...]
 
 n이 5일 때 5+8+13 = 26,
 n이 6일 떄 8+13+21 = 42
 식으로 바꿔보면 dp[n] + dp[n+1] + dp[n+2]
 
'''