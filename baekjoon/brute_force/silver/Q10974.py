## 모든 순열 (실버 3)

from itertools import permutations

cnt = int(input())

lst = [i for i in range(1, cnt+1)]

tmp = list(permutations(lst, cnt))

for i in tmp:
    print(*i)
    
## 다른 풀이
#  참고 블로그 https://honggom.tistory.com/115
n = int(input())
temp = []

def dfs():
    if len(temp) == n:
        print(*temp)
        return
    for i in range(1, n + 1):
        if i not in temp:
            temp.append(i)
            dfs()
            temp.pop()

dfs()