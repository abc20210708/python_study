## 거스름돈 (실버 5)
#  참고 블로그 https://wandukong.tistory.com/15

n = int(input())
dp = [-1, -1, 1, -1, 2, 1, 3, 2, 4, 3]
for i in range(10,n+1):
    dp.append(dp[i-5]+1)

print(dp[n])