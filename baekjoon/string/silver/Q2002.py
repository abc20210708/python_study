## 추월 (실버 1)

import sys
input = sys.stdin.readline

n = int(input())

tmp1, tmp2 = [], []

for _ in range(n):
    tmp1.append(input().rstrip())

for _ in range(n):
    tmp2.append(input().rstrip())
    
num1, num2 = 0, 0

num2 = tmp2.index(tmp1[0])

print(num2 - num1)