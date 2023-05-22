## 2xn 타일링 2 (실버 3) *
# 참고 블로그 https://bgeun2.tistory.com/68

import sys
n = int(sys.stdin.readline())

d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2] * 2) % 10007
    
print(d[n])