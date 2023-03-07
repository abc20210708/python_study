# 프린터

## 참고 블로그 https://hwisaek.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%94%84%EB%A6%B0%ED%84%B0-Python

'''
def solution(p, location):
    result = 0
    
    while len(p) > 0:
        if p[0] == max(p): # 우선순위 확인
            # 맨 앞 문서 인쇄
            p.pop(0)
            result += 1
            if location == 0: # 요청한 문서이면 종료
                break
        else:
            # 맨 앞 문서를 대기 목록의 가장 마지막에 추가
            p.append(p.pop(0))
        # 요청 문서 위치 변경
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
        
          
#print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))