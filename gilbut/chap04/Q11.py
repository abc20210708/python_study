## 3진법 뒤집기

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
