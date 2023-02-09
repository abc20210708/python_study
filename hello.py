
# 상하좌우 다시 풀기

# n을 입력받기
n = 5
x, y = 1, 1
data = ["R", "R", "R", "U", "D", "D"]

#    상 하  좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['U','D','L','R']

for d in data:
    v = move_types.index(d)
    if (x + dx[v]) < 1 or (y + dy[v]) < 1:
        continue
    else:
        x += dx[v]
        y += dy[v]
        
print('x={}, y={}'.format(y, x))
