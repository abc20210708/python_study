## 통계학 (실버 3)

import sys
input = sys.stdin.readline

arr = []
total = 0
cnt = dict()

n = int(input())
for _ in range(n):
    x = int(input())
    arr.append(x)
    
    total += x
    
    if x not in cnt:
        cnt[x] = 1
    else:
        cnt[x] += 1

arr.sort()  

# 산술평균
print(round(total/n))

# 중앙값
print(arr[n//2])

# 최빈값
tmp = max(cnt.values())
nums = []
for key, value in cnt.items():
    if value == tmp:
        nums.append(key)

if len(nums) == 1:
    print(nums[0])
else:
    print(sorted(nums)[1])
    
# 범위
print(arr[-1]-arr[0])
