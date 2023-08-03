## 가장 긴 감소하는 부분 수열 (실버 2)

n = int(input())
nums = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for k in range(i):
        if nums[i] < nums[k]:
            dp[i] = max(dp[i], dp[k]+1)
               
print(max(dp))