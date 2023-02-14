
# 큰 수의 법칙 다시 풀기

# 배열의 크기 N, 숫자 더해지는 횟수 M, 그리고 연속할 수 있는 수 K
n, m, k = 5, 7, 2
arr = [3, 4, 3, 4, 3]

arr.sort()

first = arr[-1]
second = arr[-2]

result = 0

cnt1 = (m // (k + 1)) * k
cnt1 += (m % (k + 1))
cnt2 = (m - cnt1)

result += cnt1 * first
result += cnt2 * second

print(result)