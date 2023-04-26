## 스위치 켜고 끄기 (실버 4) *

# 참고 블로그 https://my-coding-notes.tistory.com/438
import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
s = [-1] + [True if s[i] == 1 else False for i in range(n)]

for _ in range(int(input())):
    g, num = map(int, input().split()) # 성별, 번호
    if g == 1:
        for i in range(num, n+1, num):
            s[i] = not s[i]
    else:
        s[num] = not s[num]
        i, j = num-1, num+1
        while 1:
            if i < 1 or j > n: break
            if s[i] == s[j]:
                s[i] = not s[i]
                s[j] = not s[j]
            else: break
            i -= 1
            j += 1

s = [-1] + list(map(int, s[1:]))
for i in range(1, n+1):
    print(s[i], end=" ")
    if i % 20 == 0:
        print()