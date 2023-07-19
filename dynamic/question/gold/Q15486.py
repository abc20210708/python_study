## 퇴사 2

# 참고 블로그 https://velog.io/@sunkyuj/python-백준-15486-퇴사-2

import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
t, p = [0] * (n+1), [0] * (n+1)

for i in range(1, n+1):
    t[i], p[i] = map(int, input().split())
    
dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = max(dp[i], dp[i-1]) # 이전까지의 최댓값
    day = i + t[i] - 1 # 당일 포함
    if day <= n: # 최종일 안으로 끝나는 경우
        # i일부터는 일을 해야하므로 i일에 얻을 수 있는 최댓값이 아닌 i-1일까지 얻을 수 있는 최댓값을 구한다
        dp[day] = max(dp[day], dp[i-1] + p[i])
        '''
        ## 다시 문제를 풀었을 때 헷갈리는 부분
        # 1. dp[day]에 값을 저장하는 것
        # 2. max에서 dp[i-1] + p[i]로 적용하는 것
             왜 dp[i] + p[i]가 아닌지           
        '''
print(max(dp))
        

'''
1. for문 생성하다가 막힘

n = int(input())
t = [0] * n
p = [0] * n

for i in range(n):
    t[i], p[i] = map(int, input().split())
    
tmp = 0
idx = 0
for i in range(n):
    
    i = idx
    if i >= n: break
    tmp += p[i]
    idx = t[i] + i
    
print(tmp)

'''

