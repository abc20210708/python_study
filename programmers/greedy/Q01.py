# 체육복

# 참고 블로그 https://iambeginnerdeveloper.tistory.com/107

def solution(n, lost, reserve):
    result = 0
    
    # 여벌 체육복이 있는 학생 중 도난 당한 학생을 제외
    reserve_del = set(reserve) - set(lost)
    
    # 체육복을 잃어버린 학생 중 여벌 체육복이 있는 학생을 제외
    lost_del = set(lost) - set(reserve)
    
    # 여벌 체육복이 있는 학생들이 도난 당한 학생들에게 체육복을 빌려줌
    for i in reserve_del:
        if i-1 in lost_del:  # 앞 번호 학생이 체육복을 잃어버렸을 경우
            lost_del.remove(i-1)  # 체육복 빌려줌
        elif i+1 in lost_del:  # 뒷 번호 학생이 체육복을 잃어버렸을 경우
            lost_del.remove(i+1)  # 체육복 빌려줌
            
    result = n - len(lost_del)  # 체육복을 잃어버린 학생 수를 전체 학생 수에서 
                                #빼면 체육 수업을 들을 수 있는 학생 수가 됨
    print(result)  # 결과 출력
        
    return result


print(solution(5, [2,3], [1,3,5]))

