## 소트인사이드 (실버 5)

import sys

s = list(map(str, sys.stdin.readline().rstrip()))

s.sort(reverse=True)
print(''.join(s))