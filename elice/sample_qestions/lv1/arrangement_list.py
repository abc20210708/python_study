## 명단 정리 

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    s = input().rstrip()
    for i in range(1, len(s)):
        if s[i].isupper():
            print(s[i:])
