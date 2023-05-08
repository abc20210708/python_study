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