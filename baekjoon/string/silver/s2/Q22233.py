## 가희와 키워드 (실버 2)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set()

for _ in range(n):
    s.add(input().rstrip())
    

for i in range(m):
    tmp = list(input().rstrip().split(","))
    cnt = len(s)
    for j in tmp:
        if j in s:
            s.remove(j)
            cnt -= 1
    print(cnt)
