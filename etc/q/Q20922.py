## 겹치는 건 싫어 (실버 1)
#  참고 블로그 https://kau-algorithm.tistory.com/709
from collections import defaultdict
import sys
input = sys.stdin.readline

n, k  = map(int, input().split())
lst = list(map(int, input().split()))

left, right = 0, 0
dd = defaultdict(int)

res = 0

while 1:
    if right == n:
        break
    if dd[lst[right]] < k:
        dd[lst[right]] += 1
        right += 1
    else:
        dd[lst[left]] -= 1
        left += 1
    res = max(right-left, res)
    
print(res)