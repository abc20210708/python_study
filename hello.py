
# 만들 수 없는 금액 다시 풀기

n = 5
data = [3, 2, 1, 1, 9]

data.sort()

target = 1


for i in data:
    if target < i:
        break
    target += i 


print(target)
    


