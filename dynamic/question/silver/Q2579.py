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
# https://chanos.tistory.com/entry/%EB%B0%B1%EC%A4%80-2579%EB%B2%88-%EA%B3%84%EB%8B%A8-%EC%98%A4%EB%A5%B4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4

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