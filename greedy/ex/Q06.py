## 무지의 먹방 라이브

import heapq

def solution(food_times,k):
    if sum(food_times) <= k:
        return -1
    tmp = k
    h = [] # 음식들을 넣어줄 heap
    l = len(food_times)
    for i in range(l):
        # 소요 시간 순서대로 음식들을 minheap에 넣어줌.
        heapq.heappush(h,(food_times[i],i+1)) 
    previous = 0 #전 음식 시간 저장
    now = 0 #현재 음식 시간 저장
    
    #다음 음식을 다 먹어치운 cycle까지 시간이 남았을 때
    while (h[0][0] - previous)*l <= tmp: 
        print(h[0][0])
        now = heapq.heappop(h)[0] #다음 음식을 뽑음
        tmp -= (now-previous) * l #남은 시간을 갱신함
        l -= 1 # 남은 음식의 수를 갱신함
        previous = now #지금 먹은 음식을 previous에 저장해줌.
        
    h = sorted(h, key=lambda x:x[1]) #index순서대로 정렬해줌.
    
    return h[tmp % len(h)][1]

print(solution([3,1,2], 5))