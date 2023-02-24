
def solution(nums):
    decimal = [False, True] + [True] * 3000
    res = 0
    sum_arr = []
    length = len(nums)
    
    for i in range(2, 200):
        for j in range(i*i, 3001, i):
            decimal[j] = False
            
    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                sum_arr.append(nums[i]+nums[j]+nums[k])
                
    for i in sum_arr:
        if decimal[i]:
            res += 1
            
    return res


print(solution([1,2,7,6,4]))
