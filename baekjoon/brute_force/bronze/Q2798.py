## 블랙잭 (브론즈 2)
#  참고 블로그 https://afterdawncoding.tistory.com/63

from itertools import permutations

n, m = map(int, input().split())
lst = list(map(int, input().split()))
tmp = set()

for three in permutations(lst, 3):
    if sum(three) > m:
        continue
    else:
        tmp.add(sum(three))
        
print(max(tmp))

