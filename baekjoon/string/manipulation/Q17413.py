# 단어 뒤집기 2

import sys
input = sys.stdin.readline

s = input().rstrip()

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