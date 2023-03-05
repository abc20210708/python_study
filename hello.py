# 다리를 지나는 트럭 다시 풀기

from collections import deque

def solution(bl, w, tw):
    q = deque([0] * bl)
    
    total_time = 0
    qSum = 0
    
    while tw:
        # 빠져 나온 트럭 무게 제거
        qSum -= q.popleft()
        total_time += 1
        
        # 현재 다리 무게 + 다음 트럭 무게가 weight를 넘으면
        if(qSum + tw[0]) > w:
            q.append(0)
        else:
            next = tw.pop(0)
            qSum += next
            q.append(next)
            
    # 다리를 빠져오지 못한 트럭 + total 시간
    return total_time + len(q)

print(solution(2, 10, [7,4,5,6]))