## Zigzag (실버 5)
#  참고 블로그 https://imzzan.tistory.com/140

n = int(input())
nums = list(map(int, input().split()))

max_len = 2
cnt = 2

for i in range(n-2):
    if nums[i] <= nums[i+1] and nums[i+1] <= nums[i+2]:
        cnt = 2
    elif nums[i] >= nums[i+1] and nums[i+1] >= nums[i+2]:
        cnt = 2
    else:
        cnt += 1
    max_len = max(max_len, cnt)
print(max_len)