## 첼시를 도와줘! (브론즈 2)
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    num = int(input())
    dic = dict()
    for _ in range(num):
        p, name = map(str, input().split())
        dic[name] = int(p)
    print(max(dic, key=dic.get))