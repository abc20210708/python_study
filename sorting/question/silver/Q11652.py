## 카드 (실버 4) *

import sys

n = int(sys.stdin.readline())
dic = {}

for i in range(n):
    x = int(sys.stdin.readline())
    if x in dic.keys():
        dic[x] += 1
    else:
        dic[x] = 1

dic = sorted(dic.items(), key=lambda x:(-x[1], x[0]))
print(dic[0][0])

## x:(-x[1], x[0])
# -x[1] 내림차순, 값이 큰 항목일수록 앞에 위치
# x[0] 오름차순, 키를 기준으로 오름차순
