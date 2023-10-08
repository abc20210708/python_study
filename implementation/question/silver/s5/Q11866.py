## 요세푸스 문제 0 (실버 5)
#  참고 블로그 https://develop247.tistory.com/358

import sys
from collections import deque

n, k = map(int, input().split())

d = deque([i for i in range(1, n+1)])

res = []
while len(d) != 0:
    for _ in range(k-1):
        d.append(d.popleft())
    res.append(str(d.popleft()))

print('<'+', '.join(res)+'>')