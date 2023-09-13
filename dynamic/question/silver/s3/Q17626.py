## Four Squares (실버 3)

# 참고 블로그 https://yuna0125.tistory.com/165
# 파이썬 제출 - 시간초과, PyPy3 제출
n = int(input())

dp = [0, 1]

for i in range(2, n+1):
    min_value = 4
    for j in range(1, int(i ** 0.5) + 1):
        min_value = min(min_value, dp[i-(j ** 2)])

    dp.append(min_value + 1)

print(dp[n])