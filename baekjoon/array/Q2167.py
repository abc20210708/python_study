## 2차원 배열의 합 (실버 5) *

# 참고 블로그 https://blog.naver.com/baeksh0330/222763534587
# 2차원 배열의 합. 브론즈 1
# dp를 이용하지 않으면 시간초과가 난다는 말을 들은거 같다. 입력받는 동시에 표를 만들어줘야 하나?
n, m = map(int, input().split())
arr=[]
dp = [[0] * (m+1)for _ in range(n+1)]
# input_data = [list(map(int, input('숫자 입력 : ').split())) for _ in range(n)] # 이렇게 한 줄로 줄일 수 있음

for _ in range(n):
    arr.append(list(map(int, input('숫자 입력 : ').split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = arr[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

k = int(input('숫자입력 k : '))

for _ in range(k):
    i, j, x, y = map(int, input('숫자 입력 : ').split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])
[출처] [파이썬/백준 2167] 2차원 배열의 합|작성자 baeksh0330