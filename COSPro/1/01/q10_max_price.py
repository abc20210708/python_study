## 문제 10) 주식으로 최대 수익을 내세요.

def solution(prices):
    # 무한대 값 설정
    INF = 1000000001
    # 이전 가격을 저장할 변수 초기화
    tmp = INF
    # 최대 이익을 저장할 변수 초기화
    answer = -INF
    # 모든 주식 가격에 대해 반복
    for price in prices:
        # 이전 가격이 무한대가 아니면
        if tmp != INF:
            # 현재 주식 가격에서 이전 가격을 뺀 값과 기존 최대 이익 중 더 큰 값을 선택하여 최대 이익 갱신
            answer = max(answer, price - tmp)
        # 이전 가격 갱신
        tmp = min(tmp, price)
    # 최대 이익 반환
    return answer

prices1 = [1, 2, 3];
ret1 = solution(prices1);

print("solution 함수의 반환 값은", ret1, "입니다.")
    
prices2 = [3, 1];
ret2 = solution(prices2);

print("solution 함수의 반환 값은", ret2, "입니다.")