## 행복한지 슬픈지 (브론즈 1)

import sys
input = sys.stdin.readline
smile = ":-)"
sad = ":-("

s = input().rstrip()
n1 = s.count(smile)
n2 = s.count(sad)

if n1 == 0 and n2 == 0:
    print("none")
elif n1 == n2:
    print("unsure")
elif n1 > n2:
    print("happy")
elif n1 < n2:
    print("sad")