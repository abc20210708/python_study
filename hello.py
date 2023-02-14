
# 큰 수의 법칙 다시 풀기

# 배열의 크기 N, 숫자 더해지는 횟수 M, 그리고 연속할 수 있는 수 K
n, m, k = 5, 8, 3
arr = [2, 4, 5, 4, 6]

arr.sort()

first = arr[-1]
second = arr[-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)