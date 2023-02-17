# GBC

# 참고 블로그 https://thflgg133.tistory.com/83

import sys


#N, M = map(int, sys.stdin.readline().split())
N, M = 3, 3

#N_section = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
N_section = [[50, 50], [40, 40], [10, 30]]
M_section = [[60, 76], [18, 28], [22, 50]]
#M_section = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
total = 0
max_diff = []


while True:
    #if N_section == [] or M_section == []:
    if len(N_section) == 0 or len(M_section) == 0:
        break
    print(f'M_section[0][0]: {M_section[0][0]}')
    print(f'N_section[0][0]: {N_section[0][0]}')
    diff_length = M_section[0][0] - N_section[0][0] # 구간 길이 차이

    if diff_length > 0: # 구간 길이 차가 양수일 때
        max_diff.append(M_section[0][1] - N_section[0][1]) 
        N_section.pop(0) 
        M_section[0][0] = diff_length # M_section[0][0] 은 두 길이의 차이값이 된다
        
    elif diff_length < 0: # 구간 길이 차가 음수일 때
        max_diff.append(M_section[0][1] - N_section[0][1])
        M_section.pop(0)
        N_section[0][0] = -diff_length # N_section[0][0] 은 두 길이의 차이값에 -가 붙은 값이 된다. (음수형태로 나오므로) 

    else: # 구간 길이 차 = 0
        max_diff.append(M_section[0][1] - N_section[0][1]) 
        M_section.pop(0)
        N_section.pop(0)

if max(max_diff) >= 0:
    print(max(max_diff))

else: # 음수 값들만 있다면 전부 다 제한 속도를 넘지 않은 것이므로 0 출력
    print(0)