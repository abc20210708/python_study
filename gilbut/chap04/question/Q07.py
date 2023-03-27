## 이상한 문자 만들기

'''
'각 단어의 짝수/홀수 번째에 따라'라는
조건이므로 카운트 변수 하나 만든 다음 진행하다 
공백 만나면 카운트 변수를 초기화
'''

# 1. 카운트 변수를 선언
def explain(s):
    s = list(s)
    cnt = 0
    # 2. 문자 배열을 순회하면서 조건에 맞게 수정
    for i in range(len(s)):
        if s[i] == ' ':
            cnt = 0 # 공백을 만나면 카운트 초기화
            continue
        s[i] = s[i].upper() if cnt % 2 == 0 else s[i].lower()
        cnt += 1
    # 3. 문자 배열을 합쳐 하나의 문자열로 만들고 반환
    return ''.join(s)