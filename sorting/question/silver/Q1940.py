## 주몽 (실버 4)

import sys
input = sys.stdin.readline

n = int(input())
target = int(input())

nums = list(map(int, input().split()))

i, j, total, cnt = 0, 0, 0, 0

while 1:
    if total >= target:
        total -= nums[i]
        i -= 1
    elif j == n:
        break
    else:
        total += nums[j]
        j += 1
    
    if total == target:
        cnt += 1
        
print(cnt)