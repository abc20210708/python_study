## 진짜 메시지 (실버 5)

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().rstrip()
    tmp = set(s)
    chk = False
    for i in tmp:
        num = s.count(i)
        if num >= 3:
            chk = True
            break
    if chk:
        print("FAKE")
    else:
        print("OK")