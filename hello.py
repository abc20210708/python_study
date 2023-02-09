
# 모험가 길드 다시 풀기

'''

'''
n = 5
data = [2, 3, 1, 2, 2]

data.sort()

cnt = 0
result = 0

for i in data:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0
    
print(result)
        
    


