## Four Squares (실버 3)

# 참고 블로그 https://yuna0125.tistory.com/165
# 파이썬 제출 - 시간초과, PyPy3 제출

n = int(input())

dp = [0, 1]

for i in range(2, n+1):
    min_value = 4 #모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 
                # 표현될 수 있다고 했기 때문에 min_value 의 초기값을 4로 지정
    for j in range(1, int(i ** 0.5) + 1): # i ** 0.5는 숫자 i의 제곱근을 계산하는 연산
        print(int(i**0.5)+1)
        min_value = min(min_value, dp[i-(j ** 2)])
        # min_value = min(min_value, dp[i-(j * j)]) 같은 코드

    dp.append(min_value + 1)

print(dp[n])
