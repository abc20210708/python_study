# 왕실의 나이트

'''
체스판과 같은 8 X 8 좌표 평면
 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동
 2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동
 
 행 위치 표현 1 ~ 8
 열 위치 표현 a ~ h
'''

# 현재 나이트의 위치 입력받기
#here = input()
here = "a1"
row = int(here[1]) #행
#column = int(ord(here[0])) - int(ord('a')) + 1 #열
column = int(ord(here[0])) - 96 #열

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), 
         (2, 1), (1, 2) ,(-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0

for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)


'''
# 참고 블로그  https://velog.io/@gabang2/%EC%99%95%EC%8B%A4%EC%9D%98-%EB%82%98%EC%9D%B4%ED%8A%B8

location = input()
location = [ord(location[0]) - 96, int(location[1])]
temp_list = [[2, 1], [2, -1], [-2, -1], [-2, 1], [1, 2], [1, -2], [-1, -2], [-1, 2]]
result = 0
for i in temp_list:
    if 1 <= location[0] - i[0] <= 8 and 1 <= location[1] - i[1] <= 8:
        result += 1

print(result)
'''

# 예제 왕실의 나이트 다시 풀기

w = "a1"
y = int(ord(w[0])) - 96
x = int(w[1])

steps = [(2, 1), (-2, 1), (-2, -1), (2, -1),
         (1, 2), (-1, 2), (-1, -2), (1, -2)]

cnt = 0

for step in steps:
    nx, ny = x + step[0], y + step[1]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    cnt += 1

print(cnt)