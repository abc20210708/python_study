## 가장 긴 증가하는 부분 수열 4 (골드 4)
#  참고 블로그 https://blogeon.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EA%B3%A8%EB%93%9C4-14002%EB%B2%88-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-4-%ED%8C%8C%EC%9D%B4%EC%8D%AC

n = int(input())
arr = list(map(int,input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+1)

a = max(dp)
print(a)

res = []
for i in range(n-1,-1,-1):
    if dp[i] == a:
        res.append(arr[i])
        a -= 1

print(*sorted(res))