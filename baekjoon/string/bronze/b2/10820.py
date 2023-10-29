## 문자열 분석 (브론즈 2)
#  참고 블로그 https://animoto1.tistory.com/entry/%EB%B0%B1%EC%A4%80-10820-%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%B6%84%EC%84%9D-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC

import sys

while 1:

    lst = sys.stdin.readline().rstrip()
    
    if not lst:
        break
    
    lower, upper, num, space = 0, 0, 0, 0
    
    for i in lst:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.isdigit():
            num += 1
        elif i.isspace():
            space += 1  
    print(lower, upper, num, space)
