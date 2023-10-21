## 내장함수

# eval()
# 수학 수식(문자열 형태) 계산 결과 반환
res = eval("(3+5)*10")
print(res)

# 정렬 sorted()
nums = [4, 7, 3, 1]

nums = sorted(nums) # 오름차순
print(nums)
nums = sorted(nums, reverse=True) # 내림차순
print(nums)

# key 속성
tmp = [('a', 40), ('b', 70), ('c', 20)]
tmp = sorted(tmp, key=lambda x:-x[1])
print(tmp)

# Counter()
from collections import Counter

cnt = Counter(['r', 'b', 'r', 'b', 'g', 'b'])

print(cnt['b']) # 'b' 등장횟수, 3
print(dict(cnt))

# r 개 데이터를 뽑아 일렬로 나열 (순열)
from itertools import permutations
data = ['A', 'B', 'C']
l = list(permutations(data, 3))
print(l)

# r개의 데이터를 뽑아 순서없이 일렬로 나열 (조합)
from itertools import combinations
l2 = list(combinations(data, 2))
print(l2)