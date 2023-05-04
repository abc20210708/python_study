## 두 개의 손 (브론즈 1) *

## 다른 풀이 1


ML, MR, TL, TR = map(lambda x:"SRP".find(x), input().split())

def lose_case(x):
    if x == 0: return 1
    elif x == 1: return 2
    else: return 0


if ML == MR and lose_case(ML) in [TL,TR]:
    print("TK")
elif TL == TR and lose_case(TL) in [ML,MR]:
    print("MS")
else:
    print("?")


## 다른 풀이 2

# 'SPR' 문자열에서 ml, mr, tl, tr 변수에 입력값에 해당하는 인덱스 값을 할당한다.
ml, mr, tl, tr = ('SPR'.index(i) for i in input().split())

# 결과 출력을 위한 변수 chk를 False로 초기화 한다.
chk = False

# 만약 ml과 mr이 같은 경우,
if ml == mr:
    # 만약 ml이 0인 경우,
    if ml == 0:
        # 만약 tl 또는 tr이 2인 경우,
        if 2 in (tl, tr):
            # 결과 출력을 위한 변수 chk를 True로 변경하고 "TK"를 출력한다.
            chk = True
            print("TK")
    else:
        # 만약 ml-1이 tl 또는 tr에 속하는 경우,
        if (ml-1) in (tl, tr):
            # 결과 출력을 위한 변수 chk를 True로 변경하고 "TK"를 출력한다.
            chk = True
            print("TK")
            
# 만약 tl과 tr이 같은 경우,
if tl == tr:
    # 만약 tl이 0인 경우,
    if tl == 0:
        # 만약 ml 또는 mr이 2인 경우,
        if 2 in (ml, mr):
            # 결과 출력을 위한 변수 chk를 True로 변경하고 "MS"를 출력한다.
            chk = True
            print("MS")
    else:
        # 만약 tl-1이 ml 또는 mr에 속하는 경우,
        if (tl-1) in (ml, mr):
            # 결과 출력을 위한 변수 chk를 True로 변경하고 "MS"를 출력한다.
            chk = True
            print("MS")
            
# 만약 결과 출력을 위한 변수 chk가 False인 경우,
if chk == False:
    # "?"를 출력한다.
    print("?")



# 참고 블로그 https://polarcompass.tistory.com/39


# 1. 두 플레이어의 가위-바위-보 움직임을 나타내는 4개의 문자를 입력받음
#    - "S"는 가위, "P"는 보, "R"은 바위를 의미함
ml, mr, tl, tr = map(lambda x:"SPR".find(x), input().split())

# 2. 입력된 문자를 0, 1, 2 중 하나의 숫자로 변환하는 함수를 정의함
#    - "S"는 0, "P"는 1, "R"은 2로 변환
def solution(x):
    return (x + 2) % 3

# 3. 만약 두 플레이어가 왼손으로 낸 움직임과 오른손으로 낸 움직임이 같고,
#    상대방이 이길 수 있는 움직임 중 하나가 자신의 두 움직임 중 하나와 일치하는 경우
#    - "TK"를 출력함 
# 4. 그렇지 않고, 두 상대방이 왼손으로 낸 움직임과 오른손으로 낸 움직임이 모두 같고,
#    자신이 이길 수 있는 움직임 중 하나가 상대방의 어느 한 손의 움직임과 일치하는 경우
#    - "MS"를 출력함 
# 5. 위의 두 경우가 모두 아닌 경우
#    - "?"를 출력함
if ml == mr and solution(ml) in [tl, tr]:
    print("TK")
elif tl==tr and solution(tl) in [ml,mr]:
    print("MS")
else:
    print("?")
