import math

# 프로그래머스 소수 만들기
def solution(nums):
    
    res = 0
    
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if (isPrime(nums[i] + nums[j] + nums[k])):
                    res += 1
    
    return res



def isPrime(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n))+ 1):
        if n % i == 0:
            return False
    
    return True

print(solution([1,2,7,6,4]))
