# 올바른 괄호

def solution(s):
    answer = True
    cnt = 0
    
    for i in s:
        if cnt < 0:
            return False
        if i == '(':
            cnt += 1
        else:
            cnt -=1
    
    if cnt < 0 or cnt > 0:
        return False

    return True