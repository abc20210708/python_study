## 하얀 칸 (브론즈 2)

tmp1 = []
tmp2 = []
total = 0

for  i in range(8):
    if i % 2 == 0:
        tmp1.append(input().rstrip())
    else:
        tmp2.append(input().rstrip())

for lst in tmp1:
    for i in range(0, len(lst), 2):
            if lst[i] == 'F':
                total += 1

for lst in tmp2:
    for i in range(1, len(lst), 2):
            if lst[i] == 'F':
                total += 1
            
print(total)