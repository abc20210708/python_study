## 주몽 (실버 4)
#  참고 블로그 https://jminie.tistory.com/108
import sys
input = sys.stdin.readline

n = int(input())
target = int(input())

nums = list(map(int, input().split()))

nums.sort()
# i - 왼, j - 오른
i, j = 0, len(nums) -1
cnt = 0


while i < j:
    total = nums[i] + nums[j]
    
    if total < target:
        i += 1
    elif total > target:
        j -= 1
    else:
        cnt += 1
        i += 1
        j -= 1
        
print(cnt)