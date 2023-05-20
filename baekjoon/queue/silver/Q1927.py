# 최소 힙 (실버 2) *
# 참고 블로그 https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-1927-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%B5%9C%EC%86%8C-%ED%9E%99-%EC%8B%A4%EB%B2%841-%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%ED%81%90
# 배열에 자연수 x 추가
# 배열에서 가장 작은 값을 출력
# 그 값을 배열에서 제거

import sys
import heapq

h = []


for _ in range(int(input())):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(h):
            print(heapq.heappop(h))
        else:
            print(0)    
    else:
        heapq.heappush(h, x)