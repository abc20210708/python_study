# 단어 뒤집기 2
## 참고 블로그 https://polarcompass.tistory.com/40

import sys
input = sys.stdin.readline

s = "<problem>17413<is hardest>problem ever<end>"

temp = ''
res = ''

for i in s:
    if i == ' ':
        if '<' not in temp :
            res += temp[::-1] + i
            temp = ''
        else:
            temp += i
    elif i == "<":
        res += temp[::-1]
        temp = ''
        temp += i
    elif i == ">":
        res += temp + i
        temp = ''
    else:
        temp += i

res += temp[::-1]

print(res)