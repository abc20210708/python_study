## 그릇 (브론즈 2)

s = input().rstrip()
total = 10

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        total += 5
    else:
        total += 10

print(total)