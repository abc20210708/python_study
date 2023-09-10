## 피보나치 비스무리한 수열 (실버 4)

n = int(input())

if n <= 3:
    print(1)
else:
    d = [0, 1, 1, 1]
    for i in range(4, n+1):
        d.append(d[i-1]+d[i-3])
    print(d[n])