## 콜라츠 추측

def solution(num):
    
    res = 0
    
    if num == 1: return 0

    while num != 1:
        res += 1
        if num % 2 == 0:
            num //= 2
        else: 
            num *= 3
            num += 1
    
    if res > 500: return -1
    
    return res