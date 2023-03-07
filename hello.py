# 전자레인지 다시 풀기
#100, 189
t = [300, 60, 10]
n = int(input())
temp = [0, 0, 0]

for i in range(len(t)):
    if n % 10 != 0:
        print(-1)
        break
    else:
        cnt = (n // t[i])
        temp[i] = cnt
        n %= t[i]

if max(temp) != 0:
    for i in temp:
        print(i, end=" ")
    

        
        
    
    
    



    
    
    


