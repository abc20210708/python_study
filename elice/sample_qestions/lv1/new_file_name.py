## 파일명 새로 저장하기

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    s = input().rstrip()
    s = s.capitalize()
    print(s)
