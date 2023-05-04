## 두 개의 손 (브론즈 1) *
# 참고 블로그 https://polarcompass.tistory.com/39


# 1. 두 플레이어의 가위-바위-보 움직임을 나타내는 4개의 문자를 입력받음
#    - "S"는 가위, "P"는 바위, "R"은 보를 의미함
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
