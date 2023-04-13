# 차량 번호판 (브론즈 1) *

'''
참고 블로그
https://codesyun.tistory.com/175

'c'는 문자가 위치하는 자리 26가지 가능
'd' 숫자가 위치하는 자리 10가지 가능

연속하는 경우 c와 d는 각각 (26-1), (10-1)가지 가능

'''

s = input()

if s[0] == 'c':
    res = 26
else:
    res = 10
    
for i in range(1, len(s)):
    if s[i] == 'c':
        if s[i -1] == 'c':
            res *= 25
        else:
            res *= 26
    else:
        if s[i-1] == 'd':
            res *= 9
        else:
            res *= 10

print(res)