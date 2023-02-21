# 피보나치 수 5

def fibo(n):
    # 종료 조건(1 혹은 2일 때 1을 반환)
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)
    
n = int(input())
print(fibo(n))

