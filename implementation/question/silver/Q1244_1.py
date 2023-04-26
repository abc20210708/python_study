# 스위치 켜고 끄기 (실버 4) 다른 풀이

# 참고 블로그
# https://dogsavestheworld.tistory.com/entry/python-%EB%B0%B1%EC%A4%80-1244%EB%B2%88-%EC%8A%A4%EC%9C%84%EC%B9%98-%EC%BC%9C%EA%B3%A0-%EB%81%84%EA%B8%B0

# 입력값 받기
n = int(input()) # 스위치의 개수
# 스위치의 초기 상태, 0번 인덱스에 -1 추가
s = [-1] + list(map(int, input().split())) 
k = int(input()) # 학생 수
# 학생들의 성별과 번호를 튜플 형태로 입력받음
students = [tuple(map(int, input().split())) for _ in range(k)] 

# 학생들의 조작에 따라 스위치 상태 변경
for g, num in students:
    # 성별이 남자일 때
    if g == 1:
        # 주어진 번호의 배수에 해당하는 스위치들의 상태를 반전시킴
        for i in range(num, n+1, num): 
            s[i] = 1 - s[i]
    # 성별이 여자일 때
    else:
        # 주어진 번호의 스위치 상태를 반전시킴
        s[num] = 1 - s[num] 
        # 해당 스위치를 중심으로 좌우로 대칭인 스위치들의 상태를 반전시킴
        for k in range(n//2): 
            if num + k > n or num - k < 1: break # 범위를 벗어나면 중단
            if s[num+k] == s[num-k]: # 대칭인 스위치들의 상태가 같으면
                s[num+k] = 1 - s[num+k] # 상태를 반전시킴
                s[num-k] = 1 - s[num-k]
            else:
                break  

# 변경된 스위치 상태 출력
for i in range(1, n+1):
    print(s[i], end=' ') # 스위치 상태 출력
    if i % 20 == 0: # 20개씩 줄바꿈
        print()