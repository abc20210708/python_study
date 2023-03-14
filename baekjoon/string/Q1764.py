# 듣보잡
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [input().strip() for i in range(n)]
b = [input().strip() for i in range(m)]

# 교차하는 이름 찾기
d = list(set(a) & set(b))

print(len(d))
for i in sorted(d):
    print(i)