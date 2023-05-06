## 무지의 먹방 라이브
# 참고 블로그 https://dante666.tistory.com/162
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

## 다른 풀이
# 참고 블로그 https://2hs-rti.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AC%B4%EC%A7%80%EC%9D%98-%EB%A8%B9%EB%B0%A9-%EB%9D%BC%EC%9D%B4%EB%B8%8C-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import heapq


def solution(food_times, K):
    answer = -1
    food = []
    for i in range(len(food_times)):
        heapq.heappush(food, (food_times[i], i+1))

    prev = 0
    l = len(food)
    while food:
        temp = (food[0][0] - prev) * l
        if K >= temp:
            K -= temp
            prev, _ = heapq.heappop(food)
            l -= 1
        else:
            index = K % l
            food.sort(key=lambda x: x[1])
            answer = food[index][1]
            break

    return answer