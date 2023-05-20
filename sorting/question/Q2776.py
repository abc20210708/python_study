## 암기왕 (실버 4)

for _ in range(int(input())):
    dic = {}
    n = int(input())
    n1 = list(map(int, input().split()))
    for i in n1:
        dic[i] = 1
    m = int(input())
    n2 = list(map(int, input().split()))
    for j in n2:
        if j in dic:
            print(1)
        else:
            print(0)