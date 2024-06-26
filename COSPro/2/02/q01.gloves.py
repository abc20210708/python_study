##  문제1) 최대한 많은 쌍의 장갑 갯수 구하기 - Python3

max_product_num = 10

def func_a(gloves):
    counter = [0 for _ in range(max_product_num + 1)]
    
    for x in gloves:
        counter[x] += 1
    return counter


def solution(left_gloves, right_gloves):
    left_counter = func_a(left_gloves)
    right_counter = func_a(right_gloves)
    
    total = 0
    
    for i in range(1, max_product_num + 1):
        total += min(left_counter[i], right_counter[i])
    return total


left_gloves = [2, 1, 2, 2, 4]
right_gloves = [1, 2, 2, 4, 4, 7]
ret = solution(left_gloves, right_gloves)

print('solution 함수의 반환 값은', ret, '입니다.')