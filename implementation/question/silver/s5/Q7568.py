## 덩치 (실버 5)
#  참고 블로그 https://velog.io/@gangjoo/Python-%EB%B0%B1%EC%A4%80-7568-%EB%8D%A9%EC%B9%98
import sys
input = sys.stdin.readline

lst = []
rank = []
n = int(input())

for _ in range(n):
    x = tuple(map(int, input().split()))
    lst.append(x)
    rank.append(1)
    
for j in range(len(lst)):
    for k in range(j+1, len(lst)):
        if lst[j][0] > lst[k][0] and lst[j][1] > lst[k][1]:
            rank[k] += 1
        elif lst[j][0] < lst[k][0] and lst[j][1] < lst[k][1]:
            rank[j] += 1

for i in rank:
    print(i, end=" ")