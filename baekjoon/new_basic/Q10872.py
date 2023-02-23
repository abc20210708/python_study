# 팩토리얼

num = int(input())

total = 1

for i in range(1, num + 1):
    total *= i

if num == 0:
    print(1)
else:
    print(total)