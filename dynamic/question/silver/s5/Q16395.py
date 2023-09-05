## 파스칼의 삼각형 (실버 5)
#  참고 블로그 https://velog.io/@seungjun123/%EB%B0%B1%EC%A4%80-16395%EB%B2%88-%ED%8C%8C%EC%8A%A4%EC%B9%BC%EC%9D%98-%EC%82%BC%EA%B0%81%ED%98%95-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC

n, k = map(int, input().split())

dp = [[] for _ in range(n)]

for i in range(n):
    for j in range(i+1):
        if i == 0 or j == 0 or j == i:
            dp[i].append(1)
        else:
            dp[i].append(dp[i-1][j-1] + dp[i-1][j])
            
print(dp[n-1][k-1])


## 다른 풀이

n, k = map(int, input().split())

t = [[0 for _ in range(n+1)] for _ in range(n+1)]
t[1][1] = 1

for i in range(2, n+1):
    for j in range(i+1):
        t[i][j] = t[i-1][j-1] + t[i-1][j]

print(t[n][k])