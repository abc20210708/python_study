## 숫자 카드 (실버 5)

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
dic = dict()
for i in lst:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

m = int(input())
tmp = list(map(int, input().split()))
for i in tmp:
    if i in dic:
        print(dic.get(i), end=" ")
    else:
        print(0, end=" ")