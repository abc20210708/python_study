# 소수

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