## 간판 (실버 5) *

import sys
input = sys.stdin.readline

def solution(a, b, name):
    for i in a:
        for j in [k for k in b if i < k]:
            step = j - i
            if name in s[i::step]:
                return 1
    return 0 

n = int(input())
name = input().rstrip()
cnt = 0

for _ in range(n):
    s = input().rstrip()
    start = [i for i in range(len(s)) if s[i] == name[0]]
    second = [i for i in range(len(s)) if s[i] == name[1]]
    cnt += solution(start, second, name)

print(cnt)