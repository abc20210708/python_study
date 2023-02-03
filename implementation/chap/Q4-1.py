
# 상하좌우

# n을 입력받기
n = int(input())
##n = 5
x, y = 1, 1
plans = input().split()
##plans = ["R", "R", "R", "U", "D", "D"]

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans :
    # 이동 후 좌표 구하기
    for i in range(len(move_types)) :
        if plan == move_types[i] :
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue
    #이동 수행
    x, y = nx, ny
    
print(x, y)




'''
n = 5

a, b = 1, 1

walk = ["R", "R", "R", "U", "D", "D"]

min_w = 2

for i in walk:
    if b < n and i == "R":
        b += 1
    elif b >= min_w and i == "L":
        b -= 1
    elif a >= min_w and i == "U":
        a -= 1
    elif a < n and i == "D":
        a += 1

print(a, b)
'''