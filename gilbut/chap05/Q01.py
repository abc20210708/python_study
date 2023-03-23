## 재귀 함수 사용
def fib_rec(n):
    if n < 3: return 1
    return fib_rec(n - 1) + fib_rec(n - 2)

## 꼬리 재귀 함수 사용
def fib_tail(n, first, second):
    if n <= 1 : return second
    return fib_tail(n - 1, second, first + second)