## 뜨거운 붕어빵 (브론즈 4)

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
for _ in range(n):
    s = list(map(str, input().rstrip()))
    s = s[::-1]
    print(''.join(s))
