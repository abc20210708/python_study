# 괄호 변환

# "균형잡힌 괄호 문자열"의 인덱스 변환
def balanced_index(p):
    cnt = 0 # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else :
            cnt -= 1
        if cnt == 0:
            return i
        
# 올바른 괄호 문자열인지 판단
def check_proper(p):
    cnt = 0 # 왼쪽 괄호의 개수
    for i in p :
        if i == '(':
            cnt += 1
        else: # cnt가 0이 된 상태에서 )가 먼저 나오면 쌍이 맞지 않음!
            if cnt == 0: # 쌍이 맞지 않은 경우 False 반환
                return False
            cnt -= 1
    return True # 쌍이 맞는 경우 True 반환

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    # "올바른 괄호 문자열"이면, v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        answer = u + solution(v)
    # 올바른 괄호 문자열이 아니라면 아래의 과정을 수행
    else :
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # 첫 번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else :
                u[i] = '('
        answer += "".join(u)
    return answer
                
    

print(solution(")("))