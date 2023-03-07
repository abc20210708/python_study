# 거스름돈 다시 풀기

coins = [500, 100, 50, 10, 5, 1]
n = 1000 - 380
cnt = 0

for i in coins:
    cnt += (n // i)
    n %= i
    
print(cnt)
    
    
    
    


