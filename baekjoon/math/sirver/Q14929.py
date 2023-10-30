## 귀찮아 (SIB) (실버 5)
#  참고 블로그 https://xxnxi.tistory.com/31

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

# 자신까지의 누적합 배열
tmp = [lst[0]]

for i in range(1, n):
    tmp.append(tmp[i-1] + lst[i])
    
# a*b + a*c = a*(b+c)를 이용
# 자신의 값 * 자신 이후의 누적합

res = 0
for i in range(n-1):
    res += lst[i] * (tmp[n-1] - tmp[i])
    # 전체 누적합 - 자신까지의 누적합
    
print(res)