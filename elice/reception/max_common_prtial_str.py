## 최장 공통 부분 문자열
## 참고 블로그  https://velog.io/@ssulee0206/%EC%B5%9C%EC%9E%A5-%EA%B3%B5%ED%86%B5-%EB%B6%80%EB%B6%84-%EB%AC%B8%EC%9E%90%EC%97%B4

A, B = input().split(" ")

dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]

A = [0] + list(A)
B = [0] + list(B)

length = 0

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] +1
        else:
            dp[i][j] = 0
        length = max(length, dp[i][j])

print(length)