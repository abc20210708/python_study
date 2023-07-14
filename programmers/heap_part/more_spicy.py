## 더 맵게

# 참고 블로그 https://velog.io/@younge/프로그래머스-더-맵게-힙

import heapq

def solution(arr, k):
    cnt = 0
    
    heapq.heapify(arr)
    
    while arr[0] < k:
        cnt += 1
        tmp = heapq.heappop(arr) + (heapq.heappop(arr) * 2)
        heapq.heappush(arr, tmp)
        if len(arr) == 1 and arr[0] < k:
            return -1
    
    return cnt

'''
다른 풀이

import heapq

def solution(arr, k):
    cnt = 0
    
    # 생성해둔 리스트를 heapif 함수를 통해
    # 즉각적으로 힙 자료형으로 변환할 수 있음 
    heapq.heapify(arr)
    
    ## 참고 블로그 https://muhly.tistory.com/78
    while arr[0] < k: # 가장 작은 수가 기준보다 낮다면 계속
        if len(arr) > 1:
            cnt += 1
            n1 = heapq.heappop(arr) 
            n2 = heapq.heappop(arr) 
            heapq.heappush(arr, n1 + n2 *2)
        else:
            return -1
    return cnt
'''

'''

1. 힙을 활용해서 문제해결 시도 
(런타임 에러 및 효율성 시간 초과)

## 참고 블로그 https://littlefoxdiary.tistory.com/3

arr = [1, 2, 3, 9, 10, 12]
k = 7
cnt = 0
# 생성해둔 리스트를 heapif 함수를 통해
# 즉각적으로 힙 자료형으로 변환할 수 있음
heapq.heapify(arr)
print(arr)

# !(문제 발견) 파이썬의 heapq 모듈에는 min 함수가 없습니다.

while min(arr) <= k:
    cnt += 1
    n1 = heapq.heappop(arr)
    n2 = heapq.heappop(arr)
    tmp = n1 + (n2 * 2)
    heapq.heappush(arr, tmp)
    
'''

'''

2. while문 수정으로 문제해결 시도 
(런타임 에러 및 효율성 시간 초과)

while 1:
    if min(arr) >= k: break
    else:
        cnt += 1
        n1 = heapq.heappop(arr)
        n2 = heapq.heappop(arr)
        tmp = n1 + (n2 * 2)
        heapq.heappush(arr, tmp)
'''