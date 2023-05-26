## 회의실 배정 (실버 1) *

import sys
input = sys.stdin.readline

# 참고 블로그 https://suri78.tistory.com/26
# https://velog.io/@oldrock1999/%EB%B0%B1%EC%A4%80-1931%EB%B2%88-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%9A%8C%EC%9D%98%EC%8B%A4-%EB%B0%B0%EC%A0%95

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[1], x[0]))
cnt = 0

last = -1

for i in arr:
    if i[0] >= last:
        cnt += 1
        last = i[1]

print(cnt)