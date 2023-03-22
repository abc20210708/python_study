## 진법 변경하기

def radixChange(num, radix):
    if num == 0 : return "0"
    nums = []
    while num:
        num, digit = divmod(num, radix)
        nums.append(str(digit))
    return ''.join(reversed(nums))
        
print(radixChange(10, 2)) 
       
'''
divmod() 함수는 
두 개의 숫자를 인자로 받아, 
첫번 째 숫자를 두번 째 숫자로 
나눈 몫과 나머지를 튜플(tuple) 형태로 반환
'''