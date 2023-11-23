## 약수 구하기

lst = []

n = int(input())

for i in range(1, n+1):
    if n % i == 0:
        lst.append(i)

print(len(lst))
for i in lst:
    print(i)