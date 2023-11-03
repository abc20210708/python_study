## 베스트셀러 (실버 4)
from collections import Counter

n = int(input())

counter = {}

for _ in range(n):
    s = input()
    if s not in counter:
        counter[s] = 1
    counter[s] += 1

#max(counter,key=counter.get) # .get 이용

# 리스트 컴프리헨션 이용
res = [k for k,v in counter.items() if max(counter.values()) == v] 
res.sort()
answer = res[0]

print(answer)

