# 카드 합체 놀이 (실버 1)

# 참고한 코드 https://www.acmicpc.net/source/52432731

import heapq

# N과 M을 입력받습니다. (카드의 개수와 작업 수)
N, M = map(int, input().split())  
# 카드의 초기 값들을 입력받습니다.
st = list(map(int, input().split()))  

def solution(M, st):
    # 리스트 st를 힙으로 변환합니다.
    heapq.heapify(st)  

    for _ in range(M):
        # st에서 가장 작은 두 값을 뽑아서 더합니다.
        x_y = heapq.heappop(st) + heapq.heappop(st)  
        heapq.heappush(st, x_y)  # 더한 결과를 다시 st에 추가합니다.
        heapq.heappush(st, x_y)  # 더한 결과를 다시 st에 추가합니다.
    return sum(st)  # st의 모든 값을 합산하여 반환합니다.

print(solution(M, st))


# 내가 작성한 코드
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

for i in range(m):
    cards.sort()
    cards[0], cards[1] = cards[0]+cards[1], cards[0]+cards[1]

print(sum(cards))

'''
heapify() 함수를 호출하면 리스트의 원소들이 
힙의 조건을 만족하도록 재정렬됩니다. 
가장 작은 원소가 인덱스 0에 위치하게 되며, 
부모 노드의 값은 항상 자식 노드의 값보다 
작아야 하는 힙의 성질을 유지합니다.

heapify() 함수를 사용하면 힙 자료구조의 
다양한 장점을 활용할 수 있습니다. 
예를 들어, heappop() 함수를 사용하여 힙에서 
가장 작은 원소를 효율적으로 추출하거나, 
heappush() 함수를 사용하여 원소를 힙에 
삽입할 수 있습니다.

따라서 heapq.heapify() 함수를 사용하면 
일반 리스트를 효율적으로 힙으로 변환하여 
다양한 힙 연산을 수행할 수 있게 됩니다.
'''