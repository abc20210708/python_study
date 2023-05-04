## 변수명 (브론즈 1) *

# 1 카멜 camelCase
# 2 스테이크 snake_case
# 3 파스칼 HowToSolveThisProblem

n, v = input().split()

if n == '2':
    tmp = v.split('_')
    s = tmp[0]
    for i in range(1,len(tmp)):
        s += tmp[i].capitalize()
    print(s)
    print(v)
    print(s[0].upper() + s[1:])

elif n == '1' or n == '3':
    tmp = []
    j = 0
    for i in range(len(v)):
        if v[i].isupper() == True and i != 0:
            tmp.append(v[j:i].lower())
            j = i
    tmp.append(v[j:].lower())
    if n == '1':
        print(v)
        print('_'.join(tmp))
        print(v[0].upper()+v[1:])
    else:
        print(v[0].lower()+v[1:])
        print('_'.join(tmp))
        print(v)