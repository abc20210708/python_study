## 카펫

# 1.전체 넓이를 구합니다.
def solution(brown, yellow):
    grid = brown + yellow
    # 최소 길이부터 정사각형까지
    for n in range(3, int(grid ** 0.5) + 1):
        if grid % n != 0 : continue
        m = grid // n
        if (n - 2) * (m - 2) == yellow:
            return [m, n]

print(solution(24, 24))