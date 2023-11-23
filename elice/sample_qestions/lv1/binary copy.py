## 진법 변환 2
import math

n, b = map(str, input().split())

n = n[::-1]
res = 0

for i in range(len(n)):
    res += (math.pow(int(b), i) * int(n[i]))
    
print(int(res))