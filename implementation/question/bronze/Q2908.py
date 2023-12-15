## 상수 (브론즈 2)

n1, n2 = map(str, input().split())
n1, n2 = n1[::-1], n2[::-1]
print(max(int(n1), int(n2)))