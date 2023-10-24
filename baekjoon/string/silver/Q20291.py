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
    
## 다른 풀이
#  https://ye5ni.tistory.com/57
N = int(input())
 
arr = []
dict = {}
 
for i in range(N):
    file = input().split('.')
    arr.append(file[1])
 
for i in arr:
    if dict.get(i):
        dict[i] += 1
    else:
        dict[i] = 1
 
dict = sorted(dict.items())
 
for i,j in dict:
    print(i,j)