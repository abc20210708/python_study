print(2 ** 4 + 11 % 5 - (20 / 2) + 13 // 2 * 3)

n1 = int(input())
n2 = int(input())

temp = 0
if n1 > n2:
    temp = n1
else:
    temp = n2

if temp % 2 == 0:
    print("더 큰 값인", temp, "은(는) 짝수입니다.")
else:
    print("더 큰 값인", temp, "은(는) 홀수입니다.")
    
