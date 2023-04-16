## 피카츄 (브론즈 1) *

import re

res = re.fullmatch('(pi|ka|chu)+', input())
print("YES" if res != None else "NO")

import sys

s = sys.stdin.readline().rstrip()

tmp = re.sub('pi|ka|chu', "", s)

if not tmp:
    print("YES")
else:
    print("NO")