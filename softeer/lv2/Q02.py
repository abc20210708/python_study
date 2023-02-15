# 8단 변속기

import sys

d = list(int, sys.stdin.readline().split())

asc = d.copy()
asc.sort()

desc = d.copy()
desc.sort(reverse=True)

if d == asc:
    print("ascending")
elif d == desc:
    print("descending")
else:
    print("mixed")