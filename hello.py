# 걸그룹 마스터 준석이(실버 3) 다시 풀기

n, m = map(int, input().split())
dic1 = {}
dic2 = {}

for _ in range(n):
    group = input()
    tmp = []
    for i in range(int(input())):
        name = input()
        dic1[name] = group
        tmp.append(name)
    tmp.sort()
    dic2[group] = tmp

for _ in range(m):
    target = input()
    num = int(input())
    if num == 1:
        print(dic1[target])
    else:
        temp = dic2.get(target)
        for i in temp:
            print(i)
