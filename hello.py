
# 럭키 스트레이트 다시 풀기

n = 123402

target = str(n)
result = 0
length = (len(target)-1) // 2 + 1

for i in range(length):
    result += int(target[i])

for i in range(length, len(target)):
    result -= int(target[i])  
    
if result == 0 :
    print("LUCKY")
else :
    print("READY")
    
                

