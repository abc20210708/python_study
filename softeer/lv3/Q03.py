## 택배 마스터 광우
#  참고 블로그 https://jie0025.tistory.com/454
from itertools import permutations
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
rails = list(map(int, input().split()))

rails_info = permutations(rails, n)

print(list(rails_info))

res = sys.maxsize

for now in rails_info:
    tmp = list(now)
    
    i = 0
    bucket = 0
    work = 0
    this_all = 0
    
    while work != k: # 작업의 수만큼 반복
        if bucket + tmp[i] <= m: # m: 바구니 무게
            bucket += tmp[i]
            tmp.append(tmp[i])
            i += 1
        else:
            this_all += bucket
            bucket = 0
            work += 1
    res = min(res, this_all)
    
print(res) 