# 지도 자동 구축

import sys

ans = 2
n = int(input())

for i in range(n):
    ans *= 2
    ans -= 1
    
print(ans * ans)