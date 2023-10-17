## 정수 삼각형 (실버 1)

## 다른 풀이
#  참고 블로그 https://coooco.tistory.com/105
import sys
n = int(sys.stdin.readline())
dp = []

for i in range(n):
  dp.append(list(map(int, input().split())))
  
for i in range(1, n):
  for j in range(i+1):
    if j == 0:
      dp[i][j] += dp[i-1][j]
    elif j == i:
      dp[i][j] += dp[i-1][j-1]
    else:
      dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
  
print(max(dp[n-1]))



#  참고 블로그 https://velog.io/@bye9/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-1932-%EC%A0%95%EC%88%98-%EC%82%BC%EA%B0%81%ED%98%952

n=int(input())
d=[]
for i in range(n):
  d.append(list(map(int, input().split())))

for i in range(1,n):
  for j in range(len(d[i])):
    if j==0:
      d[i][j]=d[i][j]+d[i-1][j]
    elif j==len(d[i])-1: 
      d[i][j]=d[i][j]+d[i-1][j-1]
    else:
      d[i][j]=max(d[i-1][j-1],d[i-1][j])+d[i][j]
print(max(d[n-1]))