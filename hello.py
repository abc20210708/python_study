
# 만들 수 없는 금액 다시 풀기

'''

'''
 
coins = [3, 2, 1, 1, 9]

num = 1

coins.sort()

for i in coins:
    if num < i:
        break
    num += i
    
print(num)
        
        
    


