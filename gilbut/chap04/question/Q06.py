## 시저 암호

def explain(s, n):
    # 1. 문자열을 배열로 만듭니다.
    s = list(s)
    '''
     2. 반복문으로 순회하면서 문자에 숫자를 더합니다.
     (현재 글자의 숫자 - 알파벳 처음 위치
     + 더해야 할 숫자) % 26 + 알파벳 처음 위치
    '''
    for i in range(len(s)):
        if s[i] == ' ': continue
        corr = ord('A') if s[i].isupper() else ord('a')
        s[i] = chr((ord(s[i]) - corr + n) % 26 + corr)
    
    return ''.join(s)


def solution(s, n):
    res = ''
    ## 32는 공백
    ##숫자는 48 ~ 57, 영문 대문자는 65 ~ 90, 영문 소문자는 97 ~ 122
    for i in s:
        if i == " ":
            res += i
        else:
            if i.islower() and ord(i) + n > 122 :
                res += chr(ord(i) - 26 + n)
            elif i.isupper() and ord(i) + n > 90:
                res += chr(ord(i) - 26 + n)
            else:
                res += chr(ord(i) + n)
    
    return res