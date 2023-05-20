## 주사위 네개 (브론즈 1)

lst = []

for _ in range(int(input())):
    tmp = sorted(list(map(int, input().split())))
    if len(set(tmp)) == 1:
        lst.append(tmp[0] * 5000 + 50000)
    if len(set(tmp)) == 2:
        if tmp[1] == tmp[2]:
            lst.append(tmp[1] * 1000 + 10000)
        else:
            lst.append((tmp[1]+tmp[2]) * 500 + 2000)
    for i in range(3):
        if tmp[i] == tmp[i+1]:
            lst.append(tmp[i] * 100 + 1000)
    lst.append(tmp[-1] * 100)

print(max(lst))
