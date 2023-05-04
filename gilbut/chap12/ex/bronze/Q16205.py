## 변수명 (브론즈 1) *

# 1 카멜 camelCase
# 2 스테이크 snake_case
# 3 파스칼 HowToSolveThisProblem

# 입력 받기
n, v = input().split()

# n이 2인 경우
if n == '2':
    # 입력받은 변수명(v)을 '_'를 기준으로 
    # 분리하여 tmp 리스트에 저장
    tmp = v.split('_')
    s = tmp[0]  # 첫번째 단어는 모두 소문자로
    # 두번째 단어부터는 첫글자만 대문자로 변경하여 s에 추가
    for i in range(1,len(tmp)):
        s += tmp[i].capitalize()
    # 변수명 출력
    print(s)
    # 입력받은 변수명 출력
    print(v)
    # 첫번째 단어만 대문자로 변경하여 출력
    print(s[0].upper() + s[1:])

# n이 1 또는 3인 경우
elif n == '1' or n == '3':
    tmp = []  # 새로운 변수명을 저장할 리스트
    j = 0  # 이전 단어의 마지막 인덱스
    for i in range(len(v)):
        # 현재 문자가 대문자이고 첫번째 문자가 아닌 경우
        if v[i].isupper() == True and i != 0:
            # 이전 단어의 마지막 인덱스부터 현재 대문자 전까지의 
            # 문자를 소문자로 변환하여 tmp에 추가
            tmp.append(v[j:i].lower())
            j = i  # j를 현재 대문자의 인덱스로 업데이트
    # 마지막 단어를 tmp에 추가
    tmp.append(v[j:].lower())
    # n이 1인 경우
    if n == '1':
        # 입력받은 변수명 출력
        print(v)
        # '_'로 구분된 단어를 합쳐서 새로운 변수명 출력
        print('_'.join(tmp))
        # 첫번째 글자만 대문자로 변경하여 출력
        print(v[0].upper()+v[1:])
    # n이 3인 경우
    else:
        # 첫번째 글자만 소문자로 변경하여 출력
        print(v[0].lower()+v[1:])
        # '_'로 구분된 단어를 합쳐서 새로운 변수명 출력
        print('_'.join(tmp))
        # 입력받은 변수명 출력
        print(v)