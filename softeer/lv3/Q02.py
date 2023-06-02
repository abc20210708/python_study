## 강의실 배정 *
# 참고 블로그 https://fre2-dom.tistory.com/19

import sys
import heapq
input = sys.stdin.readline


n = int(input())
heap = []

for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(heap, (b, a))

# 초기값
num = 0
# 강의 수
cnt = 0

while heap:
    end, start = heapq.heappop(heap)

    # 시작시간이 초기값(종료시간)보다 크거나 같으면 카운트
    # 다음 기준값은 종료시간으로 초기화
    if start >= num:
        cnt += 1
        num = end

print(cnt)
