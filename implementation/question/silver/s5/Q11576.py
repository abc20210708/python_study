## Base Conversion (실버 5)
#  참고 블로그 https://jae04099.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-11576-Base-Conversion
import math

a, b = map(int, input().split())
n = int(input())
lst = list(map(int, input().split()))
tmp = 0
res = []
fin = ''

for i in range(n):
    tmp += int(lst[i] * math.pow(a, n- i -1))

while tmp:
    num = tmp % b
    res.append(str(num))
    tmp //= b
    
res = res[::-1]
fin = ' '.join(res)
print(fin)