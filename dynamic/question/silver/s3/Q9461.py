## 파도반 수열 (실버 3)

t = int(input())

d = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(11, 101):
    d.append(d[i-2]+d[i-3])
    
for _ in range(t):
    n = int(input())
    print(d[n])