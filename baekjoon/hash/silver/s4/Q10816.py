## 숫자 카드 2 (실버 4)

n = int(input())
lst = list(map(int, input().split()))
dic = dict()

for i in lst:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
        
m = int(input())
lst2 = list(map(int, input().split()))

for i in lst2:
    if i in dic:
        print(dic.get(i), end=" ")
    else:
        print(0, end=" ")