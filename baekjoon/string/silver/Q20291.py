## 파일 정리 (실버 3)

import sys
input = sys.stdin.readline

n = int(input())
dic = dict()

for _ in range(n):
    string, tmp = input().split(".")

    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1
        
dic_keys = sorted(dic.keys())

for k in dic_keys:
    print(k.rstrip(), dic.get(k))
