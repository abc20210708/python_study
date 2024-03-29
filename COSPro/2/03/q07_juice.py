##  문제7) 남은 재료로 주스 만들기
#   참고 블로그 https://m.blog.naver.com/jeupa/222434755330

def solution(num_apple, num_carrot, k):
    
    res = 0
    
    # 사과, 당근으로 만들 수 있는 주스 개수 구하기
    if num_apple < (num_carrot * 3):
        res = num_apple // 3 # 사과가 당근보다 3배 많으면 사과 3개당 1잔씩 만들 수 있음
    else:
        res = num_carrot # 아니면 당근 1개당 1잔씩 만들 수 있음
        
    num_apple -= res * 3 # 주스 만들 떄 사과는 3개 필요하므로 (잔*3)개씩 빼기
    num_carrot -= res # 당근은 한 장당 1개씩 필요하므로 잔 수만큼 뺌
    
    
    i = 0 # 주스 1잔을 포기하고 나온 4개 재료 중, 몇 개를 토끼에게 줬는지 세는 변수
    k = k - (num_apple + num_carrot) # 토끼 먹이로 부족한 물량 수
    
    while k  > 0: # 토끼 먹이로 부족한 물량이 1개 이상 있을 때
        if i % 4 == 0: # (주스 1잔을 포기하고 얻은) 4개의 재료가 0개인가?
            res -= 1 # 그럼 주스 하나 더 포기
        i += 1 # 토끼 먹이로 재료 하나 추가
        k -= 1 # 토끼 먹이로 부족한 물량 1개는 뻄
        
    return res

print(solution(10, 5, 4))