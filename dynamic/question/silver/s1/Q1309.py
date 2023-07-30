## 동물원 (실버 1)
#  참고 블로그 https://great-park.tistory.com/131

import sys
input = sys.stdin.readline

n = int(input())
dp = [1,3] + [0]*(n-1)
for i in range(2,n+1):
    dp[i] = (dp[i-2] + dp[i-1]*2)%9901
print(dp[n])

'''

n = int(input())

if n == 1:
    print(3)
else:
    dp = [1] * (n+1)
    dp[1], dp[2] = 3, 7
    
    for i in range(3, n+1):
        dp[i] = (2 * dp[i-1] + dp[i-2]) % 9901
    print(dp[n])

'''