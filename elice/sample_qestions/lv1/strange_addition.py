## 이상한 덧셈

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    num1, num2 = map(str, input().split())
    tmp1, tmp2 = num1[::-1], num2[::-1]
    number = str(int(tmp1) + int(tmp2))
    print(number[::-1])
    