# 제로
import sys
input = sys.stdin.readline

n = int(input())

s = []
for i in range(n):
    temp = int(input())
    if temp == 0:
        s.pop()
    else:
        s.append(temp)

print(sum(s))