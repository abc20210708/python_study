## 포도주 시식 (실버 1) - 2156

# 참고 블로그 https://myjamong.tistory.com/313
#            https://velog.io/@bye9/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-2156-%ED%8F%AC%EB%8F%84%EC%A3%BC-%EC%8B%9C%EC%8B%9D

n = int(input())
wine = [0] + [int(input()) for _ in range(n)]

dp = [0] * (n+1)
dp[1] = wine[1]
if n > 1:
    dp[2] = wine[1] + wine[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-2]+wine[i], dp[i-1], dp[i-3]+wine[i-1]+wine[i])

print(dp[n])

''' # 참고 블로그 https://myvelop.tistory.com/139

wine = [0, 6, 10, 13, 9, 8, 1]
dp = [0] * (n+1)
dp[1] = wine[1]

# n의 범위가 1이상이므로 예외 분기를 넣어야한다.
if n > 1:
    dp[2] = wine[1] + wine[2]

# 점화식 도출
dp[3] = max(dp[1] + wine[3], dp[2], dp[0]+wine[2]+wine[3])
dp[4] = max(dp[2] + wine[4], dp[3], dp[1]+wine[3]+wine[4])

# 점화식은 dp[i] = max(dp[i-2]+wine[i], dp[i-1], dp[i-3]+wine[i-1]+wine[i]) 이다.

'''



n = int(input())
arr = [0] * 10000
for i in range(n):
    arr[i] = int(input())
    
d = [0] * 10000
d[0] = arr[0]
d[1] = arr[0] + arr[1]
d[2] = max(arr[2] + arr[0], arr[2]+arr[1], d[1])

for i in range(3, n):
    d[i] = max(arr[i] + d[i-2], arr[i]+arr[i-1]+d[i-3], d[i-1])
    