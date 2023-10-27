## 모음의 개수 (브론즈 4)

import sys
input = sys.stdin.readline

while 1:
    s = input().rstrip()
    total = 0
    tmp = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if s == '#':
        break
    for i in s:
        if i in tmp:
            total += 1
    print(total)