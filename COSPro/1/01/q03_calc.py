## 문제3) 계산기 by 문자열

def func_a(numA, numB, exp):
    if exp == "+":
        return numA + numB
    elif exp == '-':
        return numA - numB
    elif exp == "*":
        return numA * numB
    
def func_b(exp):
    for idx, value in enumerate(exp):
        if value == "+" or value == "-" or value == "*":
            return idx
        
def func_c(exp, idx):
    numA = int(exp[:idx])
    numB = int(exp[idx+1 :])
    return numA, numB

def solution(expression):
    exp_idx = func_b(expression)
    first_num, second_num = func_c(expression, exp_idx)
    res = func_a(first_num, second_num, expression[exp_idx])
    return res


expression = "123+12"
ret = solution(expression)

print("solution 함수의 반환 값은", ret, "입니다.")