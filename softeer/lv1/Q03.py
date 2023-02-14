#주행거리 비교하기

import sys

a, b = map(int, sys.stdin.readline().split())

if a > b:
    print("A")
elif a == b:
    print("same")
else:
    print("B")