# 문자열 다루기 기본
import re

def explain(s):
    return len(s) in {4, 6} and bool(re.match('^[0-9]*$', s))

# 숫자만 있는지 ^[0-9]*$
# 알파벳만 있는지 ^[a-zA-z]*$
# 한글만 있는지 ^[가-힣]*$

def solution(s):
    
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i.isalpha():
                return False
    else:
        return False
                
    
    return True