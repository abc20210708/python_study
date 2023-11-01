## 수익 (실버 2)
import sys
input = sys.stdin.readline

while 1:
    n = int(input())
    if n == 0:
        break
    tmp = [int(input()) for _ in range(n)]
    for i in range(1, n):
        tmp[i] = max(tmp[i],tmp[i] + tmp[i-1])
    print(max(tmp))
    