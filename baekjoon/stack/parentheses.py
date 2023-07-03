# 올바른 괄호

def solution(s):
    answer = True
    cnt = 0  # 괄호의 개수를 세는 변수

    for i in s:  # 문자열 s의 각 문자를 순회
        if cnt < 0:  # cnt가 0보다 작으면 
            # 올바른 괄호가 아니므로 False를 반환
            return False
        if i == '(':  # 현재 문자가 '('인 경우
            cnt += 1  # cnt를 1 증가시킴 (여는 괄호)
        else:  # 현재 문자가 ')'인 경우
            cnt -= 1  # cnt를 1 감소시킴 (닫는 괄호)

    if cnt < 0 or cnt > 0:  # 반복문 종료 후 cnt가
        #0보다 작거나 크면 올바른 괄호가 아니므로 False를 반환
        return False

    return True  # 모든 문자 순회 후 cnt가 0인 
                # 경우에만 올바른 괄호이므로 True를 반환