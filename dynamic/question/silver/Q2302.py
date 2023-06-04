## 극장 좌석 (실버 1) *

# 참고 코드 https://www.acmicpc.net/source/53662484

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
vip = [False] * (N+1)

for _ in range(M):
    vip[int(sys.stdin.readline())] = True

dp = [0] * (N+1)
dp[0] = 1
dp[1] = 1

for i in range(2, N+1):
    # 만약 자리를 바꿀 수 없는 좌석이면
    if vip[i]: dp[i] = dp[i-1]
    elif vip[i-1]: dp[i] = dp[i-1]
    else:
        if vip[i-2]: dp[i] = dp[i-1]*2
        else: dp[i] = dp[i-1]+dp[i-2]
    
print(dp[-1])






# 참고 블로그 https://codedrive.tistory.com/432
# https://parase.tistory.com/9

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())


if n >= 2:
    dp = [1] * (n + 1)
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]
    start = 1
    res = 1
    for _ in range(m):
        vip = int(input())
        res *= dp[vip - start]
        start = vip + 1
    print(res * dp[n - start + 1])
else:
    for _ in range(m):
        vip = int(input())
    print(1)

# 참고 블로그 https://msj725.tistory.com/129
# https://mygumi.tistory.com/132

import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
sit = [0]
count = [0]
# vip 석이 없으면 n 대입
if m == 0:
  count.append(n)
for i in range(1,m+1):
  sit.append(int(input()))
  # vip 앞전으로 앉을 수 있는 자릿수
  count.append(sit[i] - sit[i - 1] - 1)
  # 마지막 남은 자릿수
  if i == m:
    count.append(n - sit[- 1])

# 점화식 (123) 4 (56) 7 (89) = 3,2,2 중 최댓값인 3의 n = n-1 + n-2 를 구한다.
maxC = max(count)
data = [1,1]

for i in range(2,maxC+1):
  data.append(data[-2]+data[-1])
  
# 출력
result = 1

for i in count:
  result = result * data[i]

print(result)