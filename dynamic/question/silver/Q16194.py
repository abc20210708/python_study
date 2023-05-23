## 카드 구매하기 2 (실버 1) *

n = int(input())
price = [0] + list(map(int, input().split()))
d = [9999999999] * (n+1)
d[0] = 0

for i in range(n+1):
    for k in range(i+1):
        d[i] = min(d[i], d[i-k] + price[k])

print(d[n])
