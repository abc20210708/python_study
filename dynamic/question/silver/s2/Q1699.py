## 제곱수의 합 (실버 2)
#  참고 블로그 https://v3.leedo.me/devs/82

n = int(input())

dp = [i for i in range(n+1)]

for i in range(2, n+1):
    for j in range(1, i+1):
        tmp = j * j
        if tmp > i:
            break
        
        if dp[i] > dp[i-tmp] + 1:
            dp[i] = dp[i-tmp] + 1

print(dp[n])