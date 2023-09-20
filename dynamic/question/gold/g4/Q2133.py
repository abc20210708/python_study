## 타일 채우기 (골드 4)
#  참고 블로그 https://animoto1.tistory.com/entry/%EB%B0%B1%EC%A4%80-2133-%ED%83%80%EC%9D%BC-%EC%B1%84%EC%9A%B0%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python
n = int(input())

dp = [0] * 31
dp[2] = 3

for i in range(4, 32, 2):
    dp[i] = dp[i-2] * 3 + sum(dp[:i-2])*2 + 2
        
print(dp[n])
