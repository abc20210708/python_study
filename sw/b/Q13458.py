## 시험 감독 (브론즈 2)
#  참고 블로그 https://khsung0.tistory.com/44

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
b, c = map(int, input().split())
res = 0

for i in range(n):
    lst[i] -= b
    res += 1
    if lst[i] > 0:
        if lst[i] % c == 0:
            res += (lst[i] // c)
        else:
            res += (lst[i] // c)+1
            
print(res)