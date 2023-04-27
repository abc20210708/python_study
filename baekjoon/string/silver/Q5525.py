## IOIOI (실버 1) *

# 참고 블로그 https://precisepost.tistory.com/93

import sys
input = sys.stdin.readline 
# 빠른 입력을 위해 sys 모듈 사용

n = int(input().rstrip()) 
m = int(input().rstrip()) 
s = input().rstrip() 

res = 0 # 결과값 초기화
cnt = 0 # 현재 IOI 패턴이 몇 번 나타났는지 저장할 변수
i = 1 # 문자열 s의 첫 번째 문자부터 차례로 비교할 인덱스 변수

while i < m -1: # i가 m-2까지 반복
    # IOI 패턴인지 확인
    if s[i-1] == "I" and s[i] == "O" and s[i+1] == 'I':
        cnt += 1 # IOI 패턴이 나타났다면 cnt 1 증가
        if cnt == n: # IOI 패턴이 n번 연속으로 나타난 경우
            cnt -= 1 # cnt 1 감소
            res += 1 # 결과값 1 증가
        i += 1 # 다음 문자 비교를 위해 i 1 증가
    else:
        cnt = 0 # IOI 패턴이 아니라면 cnt 초기화
    i += 1 # 다음 문자 비교를 위해 i 1 증가

print(res) # 결과값 출력