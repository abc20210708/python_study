## 절댓값 힙 (실버 1) *
# 참고 블로그 https://duckracoon.tistory.com/entry/%EB%B0%B1%EC%A4%80-11286-%EC%A0%88%EB%8C%93%EA%B0%92-%ED%9E%99-%ED%95%B4%EC%84%A4-python
# https://www.jongung.com/290
import heapq
import sys

heap = []

for _ in range(int(input())):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else: # 힙에서 최소값을 꺼내어 출력
            print(heapq.heappop(heap)[1]) 
    else:  # 입력값의 절댓값과 원래값을 힙에 추가
        heapq.heappush(heap, (abs(x), x))