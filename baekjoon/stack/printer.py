# 프린터
'''
def solution(p, location):
    result = 0
    
    while len(p) > 0:
        if p[0] == max(p):
            p.pop(0)
            result += 1
            if location == 0:
                break
        else:
            p.append(p.pop(0))
        location = location -1 if location > 0 else len(p) -1
        
    return result
'''

from collections import deque

def solution(p, location):
    queue = deque(p)
    res = 0
    
    while queue:
        first = max(queue)
        cur = queue.popleft()
        location -= 1
        
        if first > cur:
            queue.append(cur)
            if location == -1:
                location = len(queue)-1
        else:
            res += 1
            if location == -1:
                break
    return res
        
            
print(solution([2, 1, 3, 2], 2))
# print(solution([1, 1, 9, 1, 1, 1], 0))