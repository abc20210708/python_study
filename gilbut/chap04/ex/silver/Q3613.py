## Java vs C++ (실버 3) *

# 참고 블로그 http://mrk0607.tistory.com/767
s = "long_and_mnemonic_identifier"
#s = input()
res = ''

if '_' in s:
    flag = 0
    if s[0] == '_' or s[-1] == '_' or '__' in s:
        res = "Error!"
    else:
        for i in s:
            if i.isupper():
                res = "Error!"
            if i == "_":
                flag = 1
                continue
            if flag == 1:
                res += i.upper()
                flag = 0
                continue
            res += i
else:
    if s[0].isupper():
        res = "Error!"
    else:
        for i in s:
            if i.isupper():
                res += "_" + i.lower()
                continue
            res += i

print(res)

'''
먼저, 입력된 문자열 s에 ''가 있는 경우를 처리합니다. 
이때, 문자열의 첫 번째 혹은 마지막 문자가 ''인 경우, 
또는 '__'가 문자열 내에 존재하는 경우는 올바른 형식이 
아니므로 'Error!'을 출력합니다. 

그렇지 않은 경우, s의 모든 문자에 대해 검사를 수행합니다. 
만약 문자가 대문자인 경우, snake_case에서는 
대문자가 사용될 수 없기 때문에 'Error!'을 출력합니다.
 
'_'가 나타나면, flag를 1로 설정하여 이후 문자가 
대문자로 시작해야 함을 나타내고, 
그 외의 문자는 그대로 추가합니다. 

flag가 1인 경우, 대문자로 변환하여 r에 추가하고, 
flag를 0으로 되돌립니다.

반면, 입력된 문자열 s에 ''가 없는 경우, 
문자열의 첫 번째 문자가 대문자인 경우도 올바른 형식이 
아니므로 'Error!'을 출력합니다. 그렇지 않은 경우, 
s의 모든 문자에 대해 검사를 수행합니다. 

만약 문자가 대문자인 경우, 
''와 해당 문자를 소문자로 변환하여 r에 추가합니다. 
그 외의 문자는 그대로 추가합니다.
'''