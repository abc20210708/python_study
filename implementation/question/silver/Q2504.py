## 괄호의 값 (실버 1)*
# 참고 블로그 https://www.jongung.com/283

import sys

input = sys.stdin.readline().rstrip()

# (()[[]])([])

# [][]((])
list = []
chk = True
val = 1
res = 0

for i, str in enumerate(input):
    if str == "(":
        list.append(str)
        val *= 2

    elif str == "[":
        list.append(str)
        val *= 3

    elif str == ")":
        if not list or list[-1] == "[":
            chk = False
            break
        if input[i-1] == "(":
            res += val
        list.pop()
        val //= 2

    elif str == "]":
        if not list or list[-1] == "(":
            chk = False
            break
        if input[i-1] == "[":
            res += val
        list.pop()
        val //= 3

if not chk or list:
    print(0)
else:
    print(res)
    
# enumerate() 참고 블로그 https://www.daleseo.com/python-enumerate/