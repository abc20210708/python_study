## 문제7) 거스름돈 구하기.

def solution(money):
    coin = [10, 50, 100, 500, 1000, 5000, 10000, 50000]
    cnt = 0
    idx = len(coin)-1
    
    while money:
        cnt += (money // coin[idx])
        money %= coin[idx]
        idx -= 1
    
    return cnt
    
money = 2760
ret = solution(money)

print("solution 함수의 반환 값은", ret, "입니다.")