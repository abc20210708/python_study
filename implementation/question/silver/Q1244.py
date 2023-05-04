## 스위치 켜고 끄기 (실버 4) *

## 다른 풀이
import sys

input = sys.stdin.readline

n = int(input()) 
s = list(map(int, input().split())) 
# 인덱스를 1부터 사용하기 위해 [-1]을 추가함.
s = [-1] + [1 if s[i] == 1 else 0 for i in range(n)] 

for _ in range(int(input())): # 조작 횟수 입력
    # 성별(1: 남학생, 2: 여학생), 번호(1부터 시작)
    g, num = map(int, input().split()) 
    if g == 1: # 남학생일 경우
        # 해당 번호의 배수인 스위치들의 상태를 반전시킴
        for i in range(num, n+1, num): 
            s[i] = 1 - s[i]
    else: # 여학생일 경우
        # 해당 번호의 스위치의 상태를 반전시킴
        s[num] = 1 - s[num] 
        # 현재 번호의 이전 번호와 이후 번호를 가리키는 변수 초기화
        i, j = num-1, num+1 
         # 이전 번호와 이후 번호의 스위치 
         # 상태가 같으면 계속해서 반전시킴
        while 1:
            # 인덱스가 범위를 벗어나면 반복 종료
            if i < 1 or j > n: break 
            # 이전 번호와 이후 번호의 스위치 상태가 같으면
            if s[i] == s[j]: 
                s[i] = 1 - s[i] # 이전 번호의 스위치 상태 반전
                s[j] = 1 - s[j] # 이후 번호의 스위치 상태 반전
            else: break # 스위치 상태가 다르면 반복 종료
            i -= 1 # 이전 번호로 이동
            j += 1 # 이후 번호로 이동

# 스위치 상태를 1과 0으로 변환하여 리스트에 저장. 
# 인덱스를 1부터 사용하기 위해 [-1]을 추가하였기 때문에 
# [1:]로 1번 인덱스부터 끝까지 슬라이싱함.
s = [-1] + list(map(int, s[1:])) 
for i in range(1, n+1): # 스위치 상태 출력
    print(s[i], end=" ") # 20개씩 출력하고 줄바꿈
    if i % 20 == 0:
        print()


# 참고 블로그 https://my-coding-notes.tistory.com/438
import sys
input = sys.stdin.readline

n = int(input()) # 스위치의 개수 입력
# 스위치의 상태 입력
s = list(map(int, input().split())) 
# 스위치의 상태를 True(켜짐) 또는 False(꺼짐)로 변환하여 리스트에 저장. 
# 인덱스를 1부터 사용하기 위해 [-1]을 추가함.
s = [-1] + [True if s[i] == 1 else False for i in range(n)] 

for _ in range(int(input())): # 조작 횟수 입력
    # 성별(1: 남학생, 2: 여학생), 번호(1부터 시작)
    g, num = map(int, input().split()) 
    if g == 1: # 남학생일 경우
        # 해당 번호의 배수인 스위치들의 상태를 반전시킴
        for i in range(num, n+1, num): 
            s[i] = not s[i]
    else: # 여학생일 경우
        # 해당 번호의 스위치의 상태를 반전시킴
        s[num] = not s[num] 
        # 현재 번호의 이전 번호와 이후 번호를 가리키는 변수 초기화
        i, j = num-1, num+1 
         # 이전 번호와 이후 번호의 스위치 
         # 상태가 같으면 계속해서 반전시킴
        while 1:
            # 인덱스가 범위를 벗어나면 반복 종료
            if i < 1 or j > n: break 
            # 이전 번호와 이후 번호의 스위치 상태가 같으면
            if s[i] == s[j]: 
                s[i] = not s[i] # 이전 번호의 스위치 상태 반전
                s[j] = not s[j] # 이후 번호의 스위치 상태 반전
            else: break # 스위치 상태가 다르면 반복 종료
            i -= 1 # 이전 번호로 이동
            j += 1 # 이후 번호로 이동

# 스위치 상태를 1과 0으로 변환하여 리스트에 저장. 
# 인덱스를 1부터 사용하기 위해 [-1]을 추가하였기 때문에 
# [1:]로 1번 인덱스부터 끝까지 슬라이싱함.
s = [-1] + list(map(int, s[1:])) 
for i in range(1, n+1): # 스위치 상태 출력
    print(s[i], end=" ") # 20개씩 출력하고 줄바꿈
    if i % 20 == 0:
        print()