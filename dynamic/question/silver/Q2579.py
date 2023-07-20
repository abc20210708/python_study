## 계단 오르기 (실버 3)

'''
1. 포도주 시식과 같은 문제라고 생각한 후
   같은 풀이로 실행 - IndexError

n = int(input())

arr = [0] * 10000

for i in range(n):
    arr[i] = int(input())

d = [0] * 10000
d[0] = arr[0]
d[1] = arr[0] + arr[1]
d[2] = max(arr[2]+arr[0], arr[2]+arr[1], d[1])

for i in range(3, n):
    d[i] = max(arr[i]+d[i-2], arr[i]+arr[i-1]+d[i-3], d[i-1])
    
print(max(d))
'''

# 참고 블로그 https://bio-info.tistory.com/158

n = int(input())
s = [int(input()) for _ in range(n)]
dp = [0] * n

if len(s) <= 2:
    print(sum(s))
else:
    dp[0] = s[0]
    dp[1] = s[0] + s[1]
    for i in range(2, n):
        dp[i] = max(dp[i-3]+ s[i-1]+s[i], dp[i-2]+s[i])
    print(dp[-1])