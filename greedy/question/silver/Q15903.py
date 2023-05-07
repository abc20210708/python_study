# 카드 합체 놀이 (실버 1)

# 내가 작성한 코드
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

for i in range(m):
    cards.sort()
    cards[0], cards[1] = cards[0]+cards[1], cards[0]+cards[1]

print(sum(cards))