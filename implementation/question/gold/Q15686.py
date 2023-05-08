## 치킨 배달 (골드 5) *
# 참고 블로그 https://juhee-maeng.tistory.com/96
from itertools import combinations

n, m = map(int, input().rstrip().split())

space = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if space[i][j] == 1: house.append((i,j))
        elif space[i][j] == 2: chicken.append((i,j))

minv = float('inf')
for ch in combinations(chicken, m):
    res = 0
    for home in house:
        res += min(abs(home[0]-i[0])+abs(home[1]-i[1]) for i in ch)
        if minv <= res:break
    if res < minv : minv = res

print(minv)


# 참고한 코드 https://www.acmicpc.net/source/53589083

import sys
import itertools

N, M = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
    # lst.append(list(map(int, sys.stdin.readline().split())))

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