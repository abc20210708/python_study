## RGB 거리 (실버 1)
# 참고 블로그 https://namhandong.tistory.com/131

import sys
input = sys.stdin.readline
# 집의 수 입력
n = int(input())

# 각 집의 RGB 비용을 저장할 리스트 생성
rgb = []

# 각 집의 RGB 비용을 입력받아 리스트에 추가
for i in range(n):
    rgb.append(list(map(int, input().rstrip().split())))

# 두 번째 집부터 마지막 집까지 반복
for i in range(1, n):
    # 현재 집을 빨강으로 칠할 경우 최소 비용: 이전 집을 초록 또는 파랑으로 칠한 경우의 최소 비용 + 현재 집을 빨강으로 칠하는 비용
    rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0]
    # 현재 집을 초록으로 칠할 경우 최소 비용: 이전 집을 빨강 또는 파랑으로 칠한 경우의 최소 비용 + 현재 집을 초록으로 칠하는 비용
    rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1]
    # 현재 집을 파랑으로 칠할 경우 최소 비용: 이전 집을 빨강 또는 초록으로 칠한 경우의 최소 비용 + 현재 집을 파랑으로 칠하는 비용
    rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1]) + rgb[i][2]

# 마지막 집까지 칠한 후 최소 비용 반환
print(min(rgb[n-1]))
