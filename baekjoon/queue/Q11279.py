## 최대 힙 (실버 2)

import heapq
import sys
heap = []

for _ in range(int(input())):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-x, x)) 
