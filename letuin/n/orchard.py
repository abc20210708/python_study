## 과수원 
'''
def solution(n, p, c):
    stock, value, total = 0, 100, 0
    for day in range(n):
        if value == 0:
            n = day
            break
        stock += p[day]
        if stock >= c[day]:
            stock -= c[day]
            total += value * c[day]
            value = 100
        else:
            value -= 20
    return f"{total/n:.2f}"

print(solution(7, [3, 4, 3, 4, 5, 0, 2], [1, 5, 3, 2, 6, 3, 2]))
'''

## 소수 n째 자리 출력 참고 블로그 https://dogsavestheworld.tistory.com/147

'''
print(f"{3.50505:.0f}") # 4
print(f"{3.50505:.1f}") # 3.5
print(f"{3.50505:.2f}") # 3.51
print(f"{3.50505:.3f}") # 3.505
'''


'''
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

1 6 4 5 8 2 2 
1 5 3 2 6 3 2
        ! * ?
        
! 구간까지는 >=, 가격은 그대로 100원
* 구간에 미치지 못함..
? 구간은 -20 적용해 80원으로 적용
        
'''       