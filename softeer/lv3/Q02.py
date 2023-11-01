## 강의실 배정 *


# 참고 블로그 https://fre2-dom.tistory.com/19
# https://esj205.oopy.io/c33db8f5-31df-462c-9249-cdfc55c9c1bb
import sys
import heapq
input = sys.stdin.readline


n = int(input())
heap = []

for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(heap, (b, a))
# 힙 자료구조로 저장: 종료 시간을 기준으로 오름차순 정렬해야 하므로 종료 시간을 앞에 둠
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





## 다른 풀이
#  참고 블로그 https://appdung-ioss.tistory.com/221
import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

lst.sort(key=lambda x:(x[1], x[0]))
res = 0
now_end = 0

for start, end in lst:
  if now_end <= start:
    now_end = end
    res += 1

print(res)
