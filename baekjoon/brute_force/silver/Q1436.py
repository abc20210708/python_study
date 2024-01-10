## 영화감독 숌 (실버 5)
## 참고 블로그 https://ji-gwang.tistory.com/231
n = int(input())
theEndNumber = 666 #종말번호
count = 0 # 종말번호를 업데이트 시켜줄 카운트값
while True: #무한반복
    if '666' in str(theEndNumber): #만약 종말번호안에 666이 포함되어 있으면
        count += 1 #해당 카운트값을 1 증가
        if count == n: #그 카운트값이 입력값과 같다면
            break #반복문 탈출
    theEndNumber += 1 #종말번호를 계속해서 1씩 증가

print(theEndNumber) #입력한 n번째의 종말번호 출력


## 다른 풀이
import sys

N = int(sys.stdin.readline())

title = 666
cnt = 0
while cnt != N:
    tmp = title
    while tmp > 0:
        if tmp % 1000 == 666:
            cnt += 1
            break
        else:
            tmp = tmp // 10
    title += 1

title -= 1
print(title)