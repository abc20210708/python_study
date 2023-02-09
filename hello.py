
# 숫자 카드 게임 min()함수를 이용해 다시 풀기

'''

'''
n, m = 3, 3
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
    
print(result)
        
    


