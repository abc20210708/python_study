# 팰린드롬 만들기 다시 풀기

import collections
import sys

input = sys.stdin.readline
word = input().strip()

chk_word = collections.Counter(word)
cnt = 0

res = ""
mid = ""

for k,v in list(chk_word.items()):
    if v % 2 == 1:
        cnt += 1
        mid = k
        if cnt > 1:
            print("I'm Sorry Hansoo")
            exit()
            
for k, v in sorted(chk_word.items()):
    res += (k * (v // 2))
print(res + mid + res[::-1])