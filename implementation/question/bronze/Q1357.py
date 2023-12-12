## 뒤집힌 덧셈 (브론즈 1)
n1, n2 = map(str, input().split())
n1 , n2= n1[::-1], n2[::-1]
res = int(n1)+int(n2)
res = str(res)[::-1]
print(int(res))