## 유학 금지 (브론즈 2)

target = ['C','A','M','B','R','I','D','G','E']

s = input()

for i in s:
    if i in target:
        s = s.replace(i, '')

print(s)