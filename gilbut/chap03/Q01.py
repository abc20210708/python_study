'''
배열

배열은 연속적으로 데이터를 집어넣을 수 있는
1차원 형식의 자료구조


# 2차원 배열일 때 원하는 값을 찾으려면
만약 데이터가 (1, 2)에 있다면
행1, 열 2 순으로 배열에 접근한다.

'''

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