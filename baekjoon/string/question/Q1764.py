# 듣보잡

## 참고 블로그 https://dojinkimm.github.io/problem_solving/2019/09/26/boj-1764-deutbo.html

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