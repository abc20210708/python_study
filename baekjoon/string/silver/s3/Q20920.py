## 영단어 암기는 괴로워 (실버 3)

'''
1. 자주 나오는 단어일수록 앞에 배치
2. 해당 단어의 길이가 길수록 앞에 배치
3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치
'''

# 영어 지문에 나오는 단어의 개수 n
# 외울 단어의 길이 기준이 되는 m
# 길이가 m이상인 단어들만 외운다고 한다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = dict()

for _ in range(n):
    s = input().rstrip()
    if len(s) >= m:
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1

tmp = sorted(dic.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))

for i, j in tmp:
    print(i)
