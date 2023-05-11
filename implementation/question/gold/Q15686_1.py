## 치킨 배달 (책 풀이)

from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c)) # 집
        elif data[c] == 2:
            chicken.append((r, c)) # 치킨 집

# 모든 치킨 집 중에서 m개의 치킨집을 뽑는 조합 계산
mixes = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(mix):
    res = 0
    # 모든 집에 대하여
    for hx, hy in house:
        # 가장 가가운 치킨집을 찾기
        temp = 1e9
        for cx, cy in mix:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨집까지의 거리 더하기
        res += temp
    # 치킨 거리의 합 반환
    return res

# 치킨 거리의 합의 최소를 찾아 출력
res = 1e9
for mix in mixes:
    res = min(res, get_sum(mix))

print(res)

'''
# 참고 블로그 https://velog.io/@0__h0__/Python-%EC%B5%9C%EC%86%8C-%EC%B5%9C%EB%8C%80-%EA%B0%92-%EC%84%A4%EC%A0%95-1e9
1e9
알고리즘 공부를 하다보면, 최소, 최대값을 구해야 하는 문제가 많다.
이때 초반에 최소, 최대값을 설정하는 방법 중에 1e9, -1e9로 설정하는 경우를 볼 수 있는데,
이 방법은 문제에서 주어진 조건 중 수의 범위가 10억 이내일 경우 사용 가능하다.

1e9 : 1*10^9 = 1,000,000,000
-1e9 : -1*10^9 = -1,000,000,000

2e9
2e9는 int내의 범위에서 최소, 최대 값을 설정할 때 사용할 수 있다.

'''