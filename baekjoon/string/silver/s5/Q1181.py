## 단어 정렬 (실버 5)

import sys

s = set()

for _ in range(int(input())):
    word = sys.stdin.readline().rstrip()
    s.add(word)

s = list(s)
s.sort()
s.sort(key=len)


for i in s:
    print(i)