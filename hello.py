# Java vs C++ 다시 풀기

import sys
target = sys.stdin.readline().rstrip()
res = ""

if '_' in target:
    chk = False
    if "__" in target or target[-1] == '_' or target[0] == '_': 
        print('Error!')
        exit()
    else:
        for i in target:
            if i.isupper():
                print("Error!")
                exit()
            if chk:
                res += i.upper()
                chk = False
                continue
            if i == "_":
                chk = True
                continue
            res += i
else:
    if target[0].isupper():
        print('Error!')
        exit()
    else:
        for i in target:
            if i.isupper():
                res += "_" + i.lower()
                continue
            res += i

print(res)     