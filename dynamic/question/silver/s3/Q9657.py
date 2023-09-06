## 돌 게임 3 (실버 3)
#  참고 블로그 https://dev-scratch.tistory.com/96

n = int(input())

tmp = ["SK", "CY"]
d = [-1] * 1001

d[1] = 0 # SK
d[2] = 1 # CY
d[3] = 0 # SK
d[4] = 0 # SK

for i in range(5, n+1):
    if d[i-1] == d[i-3] == d[i-4] == 0:
        d[i] = 1
    else:
        d[i] = 0

print(tmp[d[n]])
