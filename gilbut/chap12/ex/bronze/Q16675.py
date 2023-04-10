# 두 개의 손 (브론즈 2) *

# 가위 S 0 , 바위 R 1 , 보 P 2
# 0 < 1< 2 & 2 < 0


ml, mr, tl, tr = ('SPR'.index(i) for i in input().split())
'''
받은 문자열을 가위(S), 바위(R), 보(P)를 
각각 0, 1, 2로 변환하여 ml, mr, tl, tr 변수에 저장합니다.
'''

if ml == mr and (ml + 2)% 3 in [tl,tr]:
    print("TK")
elif tl == tr and (tl + 2)%3 in [ml,mr]:
    print("MS")
else:
    print("?")
    
'''
먼저 가위, 바위, 보 입력을 0, 1, 2 로 받는다.

1은 0을 이기고 2는 1을 이기고 다시 0은 2를 이긴다.

만약, 한명이 두 손 다 같은 걸 내고, 상대방이 
이기는 걸 하나라도 가지고 있다면 상대방이 무조건 이긴다. 
그렇지 않은 경우에는 물음표를 출력하면 된다.

참고 블로그 https://blog.naver.com/962300/222329061934
'''