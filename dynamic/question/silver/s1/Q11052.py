## 카드 구매하기 (실버 1) *
# 참고 블로그 https://soy3on.tistory.com/301?category=730426
# https://velog.io/@hope1213/%EB%B0%B1%EC%A4%80-11052-%EC%B9%B4%EB%93%9C-%EA%B5%AC%EB%A7%A4%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
n = int(input())  # 카드 개수를 입력받는다.
card = [0] + list(map(int, input().split()))  # 인덱스를 맞추기 위해 0을 추가한 뒤 카드 가격들을 리스트로 입력받는다.

d = [0] * (n+1)  # 최대 가격을 저장할 DP 테이블을 0으로 초기화한다.

for i in range(1, n+1):  # 1장부터 n장까지의 카드 구매에 대해 최대 가격을 계산한다.
    for k in range(1, i+1):  # 1장부터 i장까지 카드를 구매하는 경우를 고려한다.
        d[i] = max(d[i], d[i-k] + card[k])  # i장의 카드를 구매하는 경우와 (i-k)장의 카드를 구매하고 k장의 카드를 추가로 구매하는 경우 중 가격이 더 높은 값을 저장한다.

print(d[n])  # n장의 카드를 구매하는데 드는 최대 가격을 출력한다.
