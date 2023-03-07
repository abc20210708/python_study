

## 참고 블로그 https://velog.io/@soo5717/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A3%BC%EC%8B%9D%EA%B0%80%EA%B2%A9-Python
'''
def solution(prices):
    n = len(prices)
    result = [0] * n # 가격이 떨어지지 않는 기간을 저장하는 배열
    stack = [] # 현재 인덱스 이전의 인덱스를 저장
    
    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
        
    while stack:
        j = stack.pop()
        result[j] = n - 1 - j
        
    return result

    
print(solution([1,2,3,2,3]))
'''
from collections import deque

def solution(prices):
    q = deque(prices)
    res = []
    
    while q:
        price = q.popleft()
        cnt = 0
        for i in q:
            cnt += 1  ## 다음에 바로 떨어지더라도 1초 후라는 
                      ## 조건이므로 비교하자마자 증가해도됨
                      # 참고 https://school.programmers.co.kr/questions/35807
            if price > i:
                break
        res.append(cnt)
    return res

print(solution([1,2,3,2,3]))

'''


주식의 가격이 [1, 2, 3, 2, 3]일 때, 
각 날짜별로 뒤에 있는 날들 중 
가격이 떨어지지 않은 기간은 각각 다음과 같습니다.

1일 때는 뒤에 있는 모든 날(2일, 3일, 4일, 5일)의 
가격이 계속 올라가므로 4일간 가격이 떨어지지 않습니다.

2일 때는 뒤에 있는 3일의 가격이 
계속 올라가므로 3일간 가격이 떨어지지 않습니다.

3일 때는 뒤에 있는 4일의 가격이 떨어지지 않고, 
마지막 5일의 가격이 떨어지지 않으므로 2일간 가격이 떨어지지 않습니다.

4일 때는 마지막 5일의 가격이 떨어지지 않으므로 
1일간 가격이 떨어지지 않습니다.

5일 때는 더 이상 뒤에 가격이 없으므로 
0일간 가격이 떨어지지 않습니다.

따라서, 가격이 떨어지지 않은 기간은 [4, 3, 2, 1, 0]입니다.

주식의 가격 prices가 매개변수로 주어질 때, 
각 주식의 가격이 떨어지지 않은 기간을 구해서 
배열로 return 하도록 solution 함수를 완성하세요.

예를 들어, [1, 2, 3, 2, 3]이라는 입력이 주어졌을 때, stack과 answer 배열의 변화는 다음과 같습니다.

i	prices[i]	stack	    answer
0	1	        [0]  	    [0, 0, 0, 0, 0]
1	2	        [0, 1]	    [0, 0, 0, 0, 0]
2	3	        [0, 1, 2]	[0, 0, 0, 0, 0]

이 문제는 최초의 시점에서부터 
최초의 떨어진시점까지의 주식 유지 시간을 나타냅니다.
애초에 시작위치에서 그 이후로 
한번이라도 떨어졌으면 그 다음에는 계산할 필요가 없습니다.

현재시점부터 얼마나 오랫동안 유지하느냐? 를 생각하시면 됩니다.
'''