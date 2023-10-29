## 추월 (실버 1)
#  참고 블로그 https://hbj0209.tistory.com/115

import sys
input = sys.stdin.readline

n = int(input())
res = 0

inn, out = dict(), []

for i in range(n):
    car = input().rstrip()
    inn[car] = i

for _ in range(n):
    out.append(input().rstrip())

for i in range(n-1):
    for j in range(i+1, n):
        if inn[out[i]] > inn[out[j]]:
            res += 1
            break

print(res)