## 카펫 *

# 1.전체 넓이를 구합니다.
def solution(brown, yellow):
    grid = brown + yellow
    # 최소 길이부터 정사각형까지
    for n in range(3, int(grid ** 0.5) + 1):
        #print(grid ** 0.5)
        if grid % n != 0 : continue
        m = grid // n
        if (n - 2) * (m - 2) == yellow:
            return [m, n]

print(solution(24, 24))

'''
int(grid ** 0.5)는 grid의 제곱근을 정수로 
내림한 값을 구하는 것입니다. 

탐색할 최소 변 길이를 3으로 설정하고, 
grid의 제곱근을 구한 뒤, 그 값을 정수로 내림하여 
최대 변 길이로 설정하는 것입니다.

'''