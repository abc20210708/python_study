## 문자열 암호화 (실버 3) *
import sys

while 1:
    n = int(input())
    if n == 0: break
    s = sys.stdin.readline().rstrip().upper()
    s = [i for i in s if i != ' ']
    dt = dict() # 문성를 연결하는 사전 dt 선언
    
    i = 0
    j = 0
    cnt = 0
    while 1:
        # 모든 문자가 사전 dt에 연결되었다면 반복 종료
        if len(s) == len(dt): break 
        if i >= len(s):
            cnt += 1
            # 한 번에 연결할 수 있는 문자 개수를 넘어가면 
            # 다음 줄로 이동
            i = cnt
        dt[i] = s[j] # 사전 dt에 연결
        i += n # 다음에 연결할 문자의 인덱스 증가
        j += 1 # 다음 문자로 이동
    # 사전 dt를 문서 번호 순으로 정렬    
    dt = sorted(dt.items(), key=lambda x: x[0])
    
    for i in dt:
        # 사전 dt의 값을 출력
        print(i[1], end="")
    print()
    
    
'''

'''
    
    