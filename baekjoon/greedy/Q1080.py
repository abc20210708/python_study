## 행렬 (실버 1) *
# 참고 블로그 https://puleugo.tistory.com/39
# https://codingpractices.tistory.com/entry/%EA%B7%B8%EB%A6%AC%EB%94%94-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%982-%EB%B0%B1%EC%A4%80-1080-%ED%96%89%EB%A0%AC-%ED%8C%8C%EC%9D%B4%EC%8D%AC


a, b = map(int, input().split()) # a, b 입력
cnt = 0 # 연산 횟수를 세는 변수 초기화

A = [list(map(int, input())) for _ in range(a)] # A 행렬 입력
B = [list(map(int, input())) for _ in range(a)] # B 행렬 입력

# x, y를 시작으로 3x3 행렬의 각 원소를 뒤집는 함수
def solution(x, y, A):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 - A[i][j]

# A 행렬을 B 행렬로 바꾸는 최소 연산 횟수 구하기
for i in range(a-2):
    for j in range(b-2):
        # A[i][j]가 B[i][j]와 다르면 연산을 진행한다.
        if A[i][j] != B[i][j]:
            solution(i, j, A) # 3x3 행렬을 뒤집는 함수 호출
            cnt += 1 # 연산 횟수 1 증가

# A 행렬과 B 행렬이 같은지 확인
flag = True
for i in range(a):
    for j in range(b):
        if A[i][j] != B[i][j]:
            flag = False
            break

# flag가 True면 연산 횟수 출력, False면 -1 출력
print(cnt) if flag else print(-1)