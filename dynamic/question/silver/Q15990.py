## 1, 2, 3 더하기 5 (실버 2) *
# 참고 블로그 https://velog.io/@yibangwon/%EB%B0%B1%EC%A4%80-15990-1-2-3-%EB%8D%94%ED%95%98%EA%B8%B0-5-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys

t = int(sys.stdin.readline())
mod = 1000000009
d = [[0 for _ in range(3)] for i in range(100001)]

d[1] = [1, 0, 0]
d[2] = [0, 1, 0]
d[3] = [1, 1, 1] # 1로 끝나느 경우 1개, 2-1, 3-1

for i in range(4, 100001):
    # 6일 때 만약
    # 5에서 2와 3으로 끝난 것에 1 붙이기. 1로 끝난 경우
    d[i][0] = (d[i - 1][1] + d[i - 1][2]) % mod
    # 4에서 1과 3으로 끝난 것에 2 붙이기. 2로 끝난 경우
    d[i][1] = (d[i - 2][0] + d[i - 2][2]) % mod
    # 3에서 1과 2로 끝난 것에 3 붙이기. 3으로 끝난 경우
    d[i][2] = (d[i - 3][0] + d[i - 3][1]) % mod


for i in range(t):
    n = int(sys.stdin.readline())
    print(sum(d[n]) % mod)

