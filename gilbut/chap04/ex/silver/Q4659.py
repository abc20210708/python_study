## 비밀번호 발음하기 (실버 5) *
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