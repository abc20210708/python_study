## 시저 암호

def solution(s, n):
    res = ''
    ## 32는 공백
    ##숫자는 48 ~ 57, 영문 대문자는 65 ~ 90, 영문 소문자는 97 ~ 122
    for i in s:
        if i == " ":
            res += i
        elif i.islower():
            if ord(i) + n > 122:
                res += chr(ord(i) - 26 + n) 
            else:
                res += chr(ord(i) + n)
        elif i.isupper():
            if ord(i) + n > 90:
                res += chr(ord(i) - 26+ n)
            else:
                res += chr(ord(i) + n)
    
    
    return res