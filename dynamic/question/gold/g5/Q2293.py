## 동전 1 (골드 5)

## 다른 풀이
#  참고 블로그 https://tesseractjh.tistory.com/132
import sys

n, k = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(n)]
dp = [1]+[0] * k 
## 0번째 인덱스가 1인 이유는 0원을 만드는 방법은 
# 동전을 하나도 사용하지 않는 경우 딱 1개 뿐이기 때문 
for value in coin:
    for i in range(1, k+1):
        if i < value: continue 
        dp[i] += dp[i-value]

print(dp[k])

'''
if i < value: continue 
예를 들어 현재 동전이 3원짜리이고, 
목표액 k는 10원이라면
dp[1], dp[2]는 목표액이 현재 동전 가치인 3원보다 작으므로 
갱신되지 않아서 그대로 0이다.
'''

#  참고 블로그 https://zu-techlog.tistory.com/48

n, k = map(int, input().split())

c = []
for _ in range(n):
    c.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1

for coin in c:
    for i in range(k+1):
        if i - coin >= 0:
            dp[i] += dp[i-coin]
            
print(dp[k])