
# 괄호 변환 다시 풀기


# 균형잡힌 괄호 문자열의 인덱스 확인
def balance_idx(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else :
            cnt -= 1
        if cnt == 0:
            return i


# 올바른 괄호 문자열인지 판단
def check_proper(p):
    cnt = 0
    for i in p:
        if i == '(':
            cnt += 1
        else :
            if cnt == 0:
                return False
            cnt -= 1
    return True




def solution(p):
    answer = ''
    if p == '':
        return answer
    
    idx = balance_idx(p)
    u = p[:idx + 1]
    v = p[idx + 1:]
    
# "올바른 괄호 문자열"이면
# v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        answer = u + solution(v)
    else :
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer

print(solution("()))((()"))