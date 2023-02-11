
# 팩토리얼 예제 다시 풀기

# 반복적으로 구현한 팩토리얼
def fac(n):
    result = 1
    # 1부터 n까지 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result

print(fac(5))
    
    
# 재귀로 구현
def fac1(n):
    if n <= 1:
        return 1
    else:
        return n * fac1(n - 1)

print(fac1(5))
                

