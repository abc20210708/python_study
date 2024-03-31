## 문제5) 음료수 마시기

def solution(money, price, n):
    answer = 0
    empty_bottle = answer = money // price
    
    while n <= empty_bottle:
        empty_bottle = empty_bottle -n
        answer += 1
        empty_bottle += 1
    return answer


money2 = 8
price2 = 2
n2 = 4
ret2 = solution(money2, price2, n2)

print("solution 함수의 반환 값은", ret2, "입니다.")