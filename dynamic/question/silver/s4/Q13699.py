## 점화식 (실버 4)

n = int(input())

d = [1, 1, 2, 5]

if n <= 3:
    print(d[n])
else:
    for i in range(4, n+1):
        d.append((d[i-1]*2)+(d[i-2]*2))
    print(d[n])