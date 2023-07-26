## 카드 구매하기 (실버 1) *
# 참고 블로그 https://soy3on.tistory.com/301?category=730426
# https://velog.io/@hope1213/%EB%B0%B1%EC%A4%80-11052-%EC%B9%B4%EB%93%9C-%EA%B5%AC%EB%A7%A4%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
n = int(input())
card = [0] + list(map(int, input().split()))

d = [0] * (n+1)

for i in range(1, n+1):
    for k in range(1, i+1):
        d[i] = max(d[i], d[i-k] + card[k])
        
print(d[n])