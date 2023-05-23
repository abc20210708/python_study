## 카드 구매하기 (실버 1) *
# 참고 블로그 https://pacific-ocean.tistory.com/66
# https://soy3on.tistory.com/301?category=730426

n = int(input())
lst = [0] + list(map(int, input().split()))

d = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for k in range(1, i+1):
        d[i] = max(d[i], d[i-k] + lst[k])
print(d[i])