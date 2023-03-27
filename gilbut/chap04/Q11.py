## 3진법 뒤집기


def radixChange(num, radix):
    if num == 0: return '0'
    nums = []
    while num:
        num, digit = divmod(num, radix)
        nums.append(str(digit))
    return ''.join(reversed(nums))

def new_solution(n):
    return int(radixChange(n, 3)[::-1], 3)
# 입력받은 숫자를 3진수로 변환한 다음, 변환된 문자열을 
# 역으로 뒤집고, 다시 10진수로 변환

print(new_solution(45))

'''
# n진수 -> 10진수
결과값은 모두 string

int(stirng, base)
ex) print(int('101', 2))
'''

import math

def solution(n):
    res = n
    temp = ""
    
    while res > 0:
        num = res % 3
        temp += str(num)
        res //= 3

    temp = temp[::-1]
    #print(temp)
    
    number = 0
    num = 0
    for i in temp:
        number += (math.pow(3, num) * int(i))
        num += 1
        
    return number
