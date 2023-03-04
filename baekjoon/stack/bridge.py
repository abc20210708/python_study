'''
주어진 문제는 일차선 다리를 건너려는 
트럭들의 순서가 주어졌을 때, 
다리를 건너기 위해 걸리는 최소 시간을 구하는 것입니다. 
다리에는 최대 bridge_length대의 트럭이 올라갈 수 있으며, 
다리는 weight 이하까지의 무게를 견딜 수 있습니다.

우선, 다리에 올라갈 수 있는 트럭의 개수가 주어졌으므로, 
현재 다리 위에 있는 트럭의 개수를 계속 추적하면서 
시간을 측정해야 합니다. 새로운 트럭이 다리에 올라가려면 
다리 위에 있는 트럭의 무게와 새로운 트럭의 무게의 합이 
weight를 넘지 않아야 합니다.

따라서, 큐를 이용하여 다리에 올라가는 
트럭과 다리를 건너는 트럭을 구현할 수 있습니다. 
큐에는 트럭의 무게와 함께 트럭이 다리에 진입한 시간도 
함께 저장합니다. 이 때, 큐의 길이가 bridge_length보다 크다면, 
가장 먼저 들어온 트럭이 다리를 건너기 위해 큐에서 제거되며, 
이 때 걸린 시간을 현재 시간에서 빼주어야 합니다.

다리에 진입할 수 없는 트럭의 경우, 
대기 트럭에 추가됩니다. 모든 트럭이 다리를 건너려면, 
마지막 트럭이 다리를 지나갈 때까지 시간이 걸리므로 
마지막 트럭이 다리를 지나간 시간을 반환하면 됩니다.

'''
from collections import deque

'''
def solution(bridge_length, weight, truck_weights):
    q = deque([0] * bridge_length)
    
    total_time = 0 # 걸리는 total 시간
    qSum = 0 # 다리 weight
    
    while truck_weights:
        qSum -= q.popleft() # 빠져나온 트럭 무게 제거
        # 트럭은 1씩 움직이므로, 
        # while문이 돌아가는 시간 만큼 time 추가
        total_time += 1 
        
        # 현재 다리 weight + 다음 트럭 무게가 weight를 넘으면
        if (qSum + truck_weights[0]) > weight:
            q.append(0) # 다리에 다음 트럭 올라갈 수 없으므로
            # 0을 추가
        
        else: #다음 트럭이 올라갈 수 있으면
            next = truck_weights.pop(0) #다음 트럭 나옴
            qSum += next # 다음 트럭 무게 추가
            q.append(next) # 다음 트럭 queue에 추가
    
    return total_time + len(q)
    # 다리를 빠져오지 못한 트럭 + total 시간
    
print(solution(2, 10, [7,4,5,6]))
'''


def solution(bl, w, tw):
    ing=[]
    time=0

    e=0
    while True:
        if e!=0: #다리지나간 트럭 제거
            ing.pop(0)

        time+=1

        if tw == [] and ing == []:
            return time

        if ing:  #건너는 트럭있을때
            sum=0
            for i in ing:
                sum+=i[0]
            if tw and sum + tw[0] <= w:                
                ing.append([tw.pop(0),0])       
        else:   #건너는 트럭 없을때
            ing.append([tw.pop(0),0])    

        e=0
        for i in ing:  #건너는 트럭들 경과시간추가
            i[1]+=1
            if i[1]==bl:
                e=i

    
print(solution(2, 10, [7,4,5,6]))