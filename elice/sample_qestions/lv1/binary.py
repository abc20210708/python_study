## 진법 변환 


n, b = map(int, input().split())

if n == 0:
    print(0)
    exit()

res = []

while n:
    res.append(str(n % b))
    n //= b

print(''.join(res[::-1]))