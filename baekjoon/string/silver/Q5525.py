## IOIOI (실버 1) *

# 참고 블로그 https://precisepost.tistory.com/93

import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
s = input().rstrip()

res = 0
cnt = 0
i = 1

while i < m -1:
    if s[i-1] == "I" and s[i] == "O" and s[i+1] == 'I':
        cnt += 1
        if cnt == n:
            cnt -= 1
            res += 1
        i += 1
    else:
        cnt = 0
    i += 1

print(res)