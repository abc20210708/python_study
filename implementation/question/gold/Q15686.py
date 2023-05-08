## 치킨 배달 (골드 5) *
# 참고 블로그 https://juhee-maeng.tistory.com/96

from itertools import combinations

n, m = map(int, input().rstrip().split())

space = [list(map(int, input().split())) for _ in range(n)]

house ,chicken = [], []
for i in range(n):
    for j in range(n):
        if space[i][j] == 1: house.append((i,j))
        elif space[i][j] == 2: chicken.append((i,j))

minv = float('inf')  # 초기 최소값을 무한대로 설정합니다.
for ch in combinations(chicken, m):
    # 현재 치킨 조합에 대한 거리의 합을 저장하는 변수
    res = 0  
    for home in house:
        # 현재 집과 치킨집 조합 간의 거리 중 
        # 가장 가까운 거리를 구하여 거리의 합을 계산
        res += min(abs(home[0] - i[0]) + abs(home[1] - i[1]) for i in ch)
        # 현재까지 계산한 거리의 합이 이미 최소값을 초과하면 
        # 더 이상 계산하지 않고 종료
        if minv <= res:
            break  
    if res < minv:
        # 현재 치킨 조합에 대한 거리의 합이 현재까지의 
        # 최소값보다 작으면 최소값을 갱신
        minv = res  

print(minv)  # 최소값을 출력

'''
이 코드에서 combinations(chicken, m)는 
chicken 리스트에서 m개의 치킨집을 선택하는 
모든 조합을 생성합니다. 

즉, 치킨집 리스트에서 m개의 치킨집을 선택하여 
가능한 모든 경우의 수를 만들어냅니다.

그런 다음, for ch in combinations(chicken, m): 
구문을 통해 각 조합을 하나씩 반복하면서 
최적의 해를 찾습니다. 

각 조합에 대해서는 집과 선택된 치킨집들 간의 거리를 
계산하여 거리의 합을 구하고, 최소값인 minv와 비교하여 
최소값을 갱신합니다.

이렇게 함으로써 combinations 함수를 사용하여 
가능한 모든 치킨집 조합을 확인하고, 
각 조합에 대한 거리를 계산하여 최적의 조합을 찾을 수 있습니다.
'''

# 참고한 코드 https://www.acmicpc.net/source/53589083

import sys
import itertools
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().rstrip().split())))
    

house, chicken = [], []

for i in range(N):
    for j in range(N):
        if lst[i][j]==1:
            house.append([i, j])
        elif lst[i][j]==2:
            chicken.append([i, j])
            
def dist(cor1, cor2):
    return abs(cor1[0]-cor2[0]) + abs(cor1[1]-cor2[1])

chicken_dist = [[dist(a, b) for a in house] for b in chicken]
m = 1e7

comb = itertools.combinations(chicken_dist, M)
for e in comb:
    m = min(m, sum([min([ee[i] for ee in e]) for i in range(len(house))]))

print(m)