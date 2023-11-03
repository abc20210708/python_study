## 비밀번호 발음하기 (실버 5) *

## 다른 풀이
# 1. 모음(a,e,i,o,u) 하나를 반드시 포함
# 2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
# 3. 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.

import sys
input = sys.stdin.readline

lst = ['a','e','i','o','u']

while 1:
    s = input().rstrip()
    chk = False
    
    # 종료 
    if s == "end":
        break
    
    # 1. 모음(a,e,i,o,u) 하나를 반드시 포함
    for i in lst:
        if i in s:
            chk = True
            break
    if not chk:
        print(f"<{s}> is not acceptable.")
        continue
    
    
    # 2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
    for i in range(len(s)-2):
        if s[i] in lst and s[i+1] in lst and s[i+2] in lst:
            chk = False
            break
        elif s[i] not in lst and s[i+1] not in lst and s[i+2] not in lst:
            chk = False
            break
    if not chk:
        print(f"<{s}> is not acceptable.")
        continue
    
    
    # 3. 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
    for i in s:
        if (i*2) in s:
            if 'ee' in s or 'oo' in s:
                chk = True
            else:
                chk = False
                break
    if not chk:
        print(f"<{s}> is not acceptable.")
    else:
        print(f"<{s}> is acceptable.")
    
    
        



## 참고 블로그 https://velog.io/@holawan/%EB%B0%B1%EC%A4%80-4659%EB%B9%84%EB%B0%80%EB%B2%88%ED%98%B8-%EB%B0%9C%EC%9D%8C%ED%95%98%EA%B8%B0-python

# 모음 받아오기
moem = ['a', 'e', 'i', 'o', 'u']

while 1:
    x = y = 0
    pswd = input()
    if pswd == 'end':
        break
    
    # 카운트
    cnt = 0
    # 모음 개수 세기
    for i in moem:
        if i in pswd:
            cnt += 1
    # 모음이 없으면 부적합
    if cnt < 1:
        print(f'<{pswd}> is not acceptable.')
        continue
    # 모음만 연속 3개 or 자음만 연속 3개인 경우 체크
    for i in range(len(pswd)-2):
        if pswd[i] in moem and pswd[i+1] in moem and pswd[i+2] in moem:
            x = 1
        elif not(pswd[i] in moem) and not(pswd[i+1] in moem) and not(pswd[i+2] in moem):
            x = 1
    if x == 1:
        print(f'<{pswd}> is not acceptable.')
        continue
    # 같은 글이 연속 두개인지 체크하지만 'e' 나 'o'는 continue
    for i in range(len(pswd)-1):
        if pswd[i] == pswd[i+1]:
            if pswd[i] == 'e' or pswd[i] == 'o':
                continue
            else:
                y = 1
    if y == 1:
        print(f'<{pswd}> is not acceptable.')
        continue
    # 예외 케이스를 통과하면 적합
    print(f'<{pswd}> is acceptable.')
    


'''
import re
import sys

while 1:
    #s = sys.stdin.readline().rstrip()
    s = "bontres"
    if s == 'end': break
    
    # s에 a,e,i,o,u 가 있는지 검사함
    case1 = len(re.findall('[aeiou]', s)) != 0
    # print(len(re.findall('[aeiou]', s)))
    
    # s에 모음과 자음(^+모음이므로 자음만 해당함) 3번 연속되는지 검사함
    case2 = len(re.findall('[aeiou]{3}|[^aeiou]{3}', s)) == 0
    #len() 함수를 사용하여, 찾아낸 패턴의 개수를 세고, 그 개수가 0인지 아닌지를 판단합니다.
    # print(len(re.findall('[aeiou]{3}|[^aeiou]{3}', s)))
    
    # ()로 묶은 그룹이 한번 더 반복되는지 검사
    case3 = len(re.findall('([a-df-np-z])\\1', s)) == 0
    print(len(re.findall('([a-df-np-z])\\1', s)))
    
    if case1 and case2 and case3:
        print(f"<{s}> is acceptable.")
    else:
        print(f"<{s}> is not acceptable.")
        
# 참고 블로그 https://velog.io/@youngcheon/%EB%B0%B1%EC%A4%80-4659-%EB%B9%84%EB%B0%80%EB%B2%88%ED%98%B8-%EB%B0%9C%EC%9D%8C%ED%95%98%EA%B8%B0-Python
'''
'''
len(re.findall('([a-df-np-z])\\1', s))
이 코드는 Python의 re (Regular Expression) 모듈을 사용하여, 
문자열 s에서 두 번 이상 연속해서 나타나는 소문자 영문자를 
찾아내는 정규 표현식입니다.

여기서 사용된 정규 표현식은 다음과 같습니다.

([a-df-np-z]): 소문자 영문자 a-d, f-n, p-z 중 하나를 캡처링 그룹으로 지정합니다. 
이때, 이 그룹의 패턴을 나타내는 괄호 () 안에 있는 [a-df-np-z]은 
a-d, f-n, p-z를 제외한 다른 영문자를 제외하기 위한 것입니다. 
이 패턴은 소문자 영문자 중에서는 매칭할 수 있는 문자들의 범위를 제한하는 역할을 합니다.

1: 첫 번째 그룹과 동일한 문자를 찾아내도록 지정합니다. 
이때, 이스케이프 문자 \를 사용하여 \1로 표현합니다. 
따라서, 이 패턴은 두 번 이상 연속해서 나타나는 문자를 찾아내게 됩니다.

결과적으로, 이 코드를 실행하면 문자열 s에서 두 번 이상 연속해서 
나타나는 소문자 영문자가 찾아져서 리스트 형태로 반환됩니다. 
예를 들어, "aabbccdd"라는 문자열에서는 ['a', 'b', 'c', 'd']가 반환됩니다.
'''