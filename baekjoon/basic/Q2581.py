# 소수

import sys, math

start = int(input())
end = int(input())

print(int(math.sqrt(end)) + 1)

nums = [True] * 10001 # 전부 소수로 초기화
nums[1] = False

for i in range(2, int(math.sqrt(end)) + 1):
    if nums[i]:
        j = 2
        while i * j <= end:
            nums[i*j] = False
            j += 1
            
total = 0

for i in range(start, end+1):
    if nums[i]:
        if total == 0:
            min_val = i
        total += i
        
if total > 0:
    print(total)
    print(min_val)
else:
    print(-1)


'''
start = int(input())
end = int(input())

nums = []
for num in range(start, end + 1):
    cnt = 0
    if num > 1:
        for i in range(2, num): # 2부터 num -1까지
            if num % i == 0:
                cnt += 1
                break 
        if cnt == 0:
            nums.append(num)
            
if len(nums) > 0:
    print(sum(nums))
    print(min(nums))
else:
    print(-1)
'''