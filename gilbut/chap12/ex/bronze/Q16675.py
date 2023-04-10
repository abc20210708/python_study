# 두 개의 손 (브론즈 2) *

# S - 가위, R - 바위, P - 보, 무조건 이기는 방법
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