## 카드 구매하기 (실버 1) *

n = int(input())
lst = [0] + list(map(int, input().split()))

d = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for k in range(1, i+1):
        d[i] = max(d[i], d[i-k] + lst[k])
print(d[i])