# 체육복

# 참고 블로그 https://iambeginnerdeveloper.tistory.com/107

def solution(n, lost, reserve):
    result = 0
    
    # 공통 요소를 제거
    reserve_del = set(reserve) - set(lost)
    lost_del = set(lost) - set(reserve)
    
    for i in reserve_del:
        if i-1 in lost_del:
            lost_del.remove(i-1)
        elif i+1 in lost_del:
            lost_del.remove(i+1)
            
    result = n - len(lost_del)
    print(result)
        
    return result


print(solution(5, [2,3], [1,3,5]))
    