## 과수원 

n = int(input())
p = list(map(int, input().split()))
c = list(map(int, input().split()))

res = 0
tmp = 100
for i in range(n):
    if p[i] >= c[i]:
        tmp = 100
        p[i+1] += p[i] - c[i]
        res += tmp * c[i]
    else:
        continue
 
'''
1 6 4 5 8 2 2 
1 5 3 2 6 3 2
        ! * ?
        
! 구간까지는 >=, 가격은 그대로 100원
* 구간에 미치지 못함..
? 구간은 -20 적용해 80원으로 적용
        
'''       