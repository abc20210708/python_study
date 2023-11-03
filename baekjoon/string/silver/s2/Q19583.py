## 싸이버 개강총회 (실버 2)
#  참고 블로그 https://fre2-dom.tistory.com/474

import sys
input = sys.stdin.readline

start, end, stream = map(str, input().split())
dic = dict()
res = dict()

for i in sys.stdin:
    time, name = i.rstrip().split()
    
    # 개총 시작 시간(포함)보다 일직 들어온 사람을 dic입력
    if time <= start:
        dic[name] = time
    # 개층 종료 시간과 스트리밍 종료 시간 사이에 들어온 사람 확인
    elif end <= time <= stream:
        # 계층 시작 시간보다 일찍 들어온 사람이면 res 입력
        if name in dic:
            res[name] = 1
            
print(len(res))