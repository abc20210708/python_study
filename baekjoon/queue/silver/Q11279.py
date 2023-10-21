## 최대 힙 (실버 2)
#  참고 블로그 https://myvelop.tistory.com/143
import heapq
import sys
heap = []

for _ in range(int(input())):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            # 힙에서 가장 작은 원소를 제거하고 그 값을 출력
            print(heapq.heappop(heap)[1])
    else:
        # 입력받은 값 x를 음수로 변환하여 (음수, 양수)의 튜플 형태로 힙에 삽입
        heapq.heappush(heap, (-x, x)) 
