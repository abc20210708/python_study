## 오타맨 고창영 (브론즈 2)

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    idx, s = map(str, input().rstrip().split())
    s = list(s)
    del s[int(idx)-1]
    print(''.join(s))