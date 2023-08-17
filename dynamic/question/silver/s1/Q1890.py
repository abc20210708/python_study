## 점프 (실버 1)
#  참고 블로그 https://dreamtreeits.tistory.com/212

import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())  # n은 게임 판의 크기

# 게임 판의 숫자들을 리스트로 저장
lst = [list(map(int, input().split())) for _ in range(n)]

# 각 칸으로의 도달 가능한 경로 개수를 저장할 DP 배열 초기화
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1  # 시작 지점은 1가지 경로로 도달 가능

# DP 배열 채우기
for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:  # 도착 지점에 도달한 경우
            print(dp[i][j])  # 가능한 경로 개수 출력
            break  # 반복문 종료
        tmp = lst[i][j]  # 현재 위치의 숫자 값

        # 오른쪽으로 이동하는 경우 처리
        if j + tmp < n:  # 이동한 위치가 판을 벗어나지 않는 경우
            dp[i][j + tmp] += dp[i][j]  # 현재 위치로부터 도달 가능한 경로 개수를 더해줌

        # 아래쪽으로 이동하는 경우 처리
        if i + tmp < n:  # 이동한 위치가 판을 벗어나지 않는 경우
            dp[i + tmp][j] += dp[i][j]  # 현재 위치로부터 도달 가능한 경로 개수를 더해줌
