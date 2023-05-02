## 누울 자리를 찾아라 (실버 5) *

# 참고 블로그 https://chagokchagock.tistory.com/16

import sys
input = sys.stdin.readline

n = int(input())
li = []
w, h = 0, 0
cnt = 0

# 가로
for i in range(n):
    li.append(list(input().rstrip()))
for i in range(n):
    cnt = 0
    for j in range(n):
        if li[i][j] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            w += 1
# 세로            
for i in range(n):
    cnt = 0
    for j in range(n):
        if li[j][i] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            h += 1
print(w, h)