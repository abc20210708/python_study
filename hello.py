
# 거스름돈 다시 풀어보기

'''
카운터에는 거스름돈으로 사용할 500, 100, 50, 10원짜리 동전이 무한히 존재한다고 가정
손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수
단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.
'''

money = 1260
coins = [10, 50, 100, 500]

coins.sort()
coins.reverse()

result = 0

for i in coins:
    result += money // i
    money %= i
    
print(result)


