# 상하좌우 다시 풀기

n = int(input())
steps = list(map(str, input().split()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

x = 1
y = 1

for step in steps:
    for i in range(len(move)):
        if step == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    
    x, y = nx, ny

print(x, y) 