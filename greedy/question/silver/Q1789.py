## 수들의 합 (실버 5)*

# 참고 블로그 https://pacific-ocean.tistory.com/80

s = int(input())
n = 1

while n * (n + 1) / 2 <= s:
    n += 1

print(n - 1)

#n * (n + 1) / 2는 1부터 n까지의 합의 공식