## 영수증 (브론즈 4)

target = int(input())
n = int(input())
res = 0

for _ in range(n):
    n1, n2 = map(int, input().split())
    res += (n1*n2)

if target == res:
    print("Yes")
else:
    print("No")