## 기타줄 (실버 4)


n, m = map(int, input().split())

a = []
for i in range(m):
    x, y = map(int, input().split())
    a.append([x, y])
    
a.sort(key=lambda x:x[0])
b = a.copy()
b.sort(key=lambda x:x[1])

n1 = n2 = n3= 0
n1 = n // 6
if n % 6 != 0 : n1 += 1
n1 = (a[0][0] * n1)
n2 = (b[0][1] * n)
n3 = (a[0][0] * (n//6)) + (b[0][1] * (n%6))

print(min(min(n1, n2), n3))