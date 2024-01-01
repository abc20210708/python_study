## 부분수열의 합 (실버 2)
#  참고 블로그 https://seongonion.tistory.com/98

import sys
from itertools import combinations

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, n+1):
    comb = combinations(arr, i)

    for x in comb:
        if sum(x) == s:
            cnt += 1

print(cnt)

## 다른 풀이
#  참고 블로그 https://velog.io/@cu1210/%EB%B0%B1%EC%A4%80-1182-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4%EC%9D%98-%ED%95%A9

N, S = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0
ans = []

def solve(start):
    global cnt
    if sum(ans) == S and len(ans) > 0:
        cnt += 1

    for i in range(start, N):
        ans.append(num[i])
        solve(i+1)
        ans.pop()

solve(0)
print(cnt)