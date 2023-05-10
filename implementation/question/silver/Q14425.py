## 문자열 집합 (실버 3) *

import sys
input = sys.stdin.readline
'''
n, m = map(int, input().split())
s = set([input() for _ in range(n)])
cnt = 0

for _ in range(m):
    t = input()
    if t in s:
        cnt += 1
print(cnt)
'''
## 다른 풀이 dictionary 사용
from itertools import count

# dictionary 사용
d = {}
count = 0
n1, n2 = map(int, input().split())

for _ in range(n1):
    data = input().strip()
    d[data] = True

for _ in range(n2):
    data = input().rstrip()
    if data in d:
        count += 1

print(count)