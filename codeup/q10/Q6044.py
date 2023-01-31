# 6044 : [기초-산술연산] 정수 2개 입력받아 자동 계산

# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 
# 자동으로 계산해보자.

a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(format(a / b, ".2f"))
print("{:.2f}".format(a/b))
