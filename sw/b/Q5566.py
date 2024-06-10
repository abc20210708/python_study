## 주사위 게임 (브론즈 2)
#  참고 블로그 https://amor-fati.tistory.com/132

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [int(input()) for _ in range(n)] # 각 칸의 지시사항
dice = [int(input()) for _ in range(m)] # 던진 주사위 번호

now = 0 # 현재 위치 idx
cnt = 0 # 주사위 던진 횟수

for i in range(m):
    # 던진 주사위 횟수 +1
    cnt += 1
    # 던진 주사위 만큼 이동
    now += dice[i]
    # 만약 도착위치 이상이면
    if now >= n-1:
        break
    # 지시사항 이동
    now += lst[now]
    # 만약 도착위치 이상이면
    if now >= n-1:
        break

print(cnt)

