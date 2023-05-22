## 1, 2, 3 더하기 3 (실버 2) 

import sys
t = int(sys.stdin.readline())
mod = 1000000009

d = [0] * 1000001
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 1000001):
    d[i] = (d[i-3] + d[i-2] + d[i-1]) % mod
    
for _ in range(t):
    x = int(sys.stdin.readline())
    print(d[x] % mod)