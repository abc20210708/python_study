## 회사에 있는 사람 (실버 5)

import sys

res = {}
for _ in range(int(input())):
    a, b = sys.stdin.readline().split()
    res[a] = b

tmp = []
for k,v in res.items():
    if v == "enter":
        tmp.append(k)

tmp = sorted(tmp, reverse=True)
print("\n".join(tmp))