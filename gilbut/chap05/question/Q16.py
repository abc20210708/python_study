## 콜라츠 추측

def collatz(num, res):
    # 시작 입력 숫자가 1일 때 / 결과가 1일 때 모두 확인
    if num == 1: return res 
    if res == 500:
        return -1
    
    # 1-1. 입력된 수가 짝수면 2로 나눕니다.
    if num % 2 == 0:
        return collatz(num // 2, res + 1)
    # 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
    elif num % 2 == 1:
        return collatz(num * 3 + 1, res + 1)
    # 결과로 나온 수에 같은 작업을 1이 될 때까지 반복
    if num == 1: return res
    
def explain(num):
    return collatz(num, 0)


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