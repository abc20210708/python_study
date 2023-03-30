## 비밀번호 발음하기 (실버 5) *
import re
import sys

while 1:
    #s = sys.stdin.readline().rstrip()
    s = "zoggax"
    if s == 'end': break
    
    # s에 a,e,i,o,u 가 있는지 검사함
    case1 = len(re.findall('[aeiou]', s)) != 0
    # print(len(re.findall('[aeiou]', s)))
    
    # s에 모음과 자음(^+모음이므로 자음만 해당함) 3번 연속되는지 검사함
    case2 = len(re.findall('[aeiou]{3}|[^aeiou]{3}', s)) == 0
    # print(len(re.findall('[aeiou]{3}|[^aeiou]{3}', s)))
    
    # ()로 묶은 그룹이 한번 더 반복되는지 검사
    case3 = len(re.findall('([a-df-np-z])\\1', s)) == 0
    # print(len(re.findall('([a-df-np-z])\\1', s)))
    
    if case1 and case2 and case3:
        print(f"<{s}> is acceptable.")
    else:
        print(f"<{s}> is not acceptable.")
        
# 참고 블로그 https://velog.io/@youngcheon/%EB%B0%B1%EC%A4%80-4659-%EB%B9%84%EB%B0%80%EB%B2%88%ED%98%B8-%EB%B0%9C%EC%9D%8C%ED%95%98%EA%B8%B0-Python