## 추월 (실버 1)

# deque 활용 풀이
# 참고 블로그 https://junior-datalist.tistory.com/344
import sys
from collections import deque

input = sys.stdin.readline

res = 0
n = int(input())
q = deque()

for i in range(n*2):
    if i < n:
        q.append(input().rstrip())
    else:
        out = input().rstrip()
        if out != q[0]:
            q.remove(out)
            res += 1
        else:
            q.popleft()

print(res)


#  참고 블로그 https://hbj0209.tistory.com/115
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