## 블랙잭 (브론즈 2)

## 다른 풀이
#  참고 블로그 https://seongonion.tistory.com/33
from itertools import combinations 

n, m = map(int, input().split())
items = list(map(int, input().split()))
comb = list(combinations(items, 3)) # combinations를 이용해 나열 가능한 조합 만들기
sum_value = []
for i in range(len(comb)):
  if sum(comb[i]) <= m: # 합한 값이 m보다 작아야하므로, 작을 때만 sum_value에 담아준다
    sum_value.append(sum(comb[i]))

sum_value.sort() # 오름차순으로 정렬해준 후 맨 뒷 값을 출력
print(sum_value[-1])


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

