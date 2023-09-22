## 알람 시계 (브론즈 3)

## 다른 풀이
#  참고한 코드 https://www.acmicpc.net/source/53612316
h, m = map(int, input().split())

if m >= 45:
    print(h, m-45)
else:
    if h == 0:
        print(23, m+15)
    else:
        print(h-1, m+15)

h, m = map(int, input().split())
## 현재 상근이가 설정한 알람 시간 H시 M분을 의미함
## 24시간 표현을 사용, 하루의 시작은 0:0(자정)
## 끝은 23:59(다음날 자정 1분 전)

## 45분 앞서는 시간으로 바꾸기

if m >= 45:
    m -= 45
    print(h, m)
else:
    if h == 0:
        h = 23
        m += 15
        print(h, m)
        exit()
    h -= 1
    m += 15
    print(h, m)
    
