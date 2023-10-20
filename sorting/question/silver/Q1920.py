## 수 찾기(실버 4)
import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
s = set(s)

m = int(input())
lst = list(map(int, input().split()))

for i in lst:
    if i in s:
        print(1)
    else:
        print(0)