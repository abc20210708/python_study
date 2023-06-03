## 모든 순열 (실버 3)

from itertools import permutations

cnt = int(input())

lst = [i for i in range(1, cnt+1)]

tmp = list(permutations(lst, cnt))

for i in tmp:
    print(*i)