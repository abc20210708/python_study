## 5와 6의 차이 (브론즈 2)

s1, s2 = map(str, input().split())

total_max = 0
total_min = 0

if '5' in s1:
    s1 = s1.replace('5', '6')
if '5' in s2:
    s2 = s2.replace('5', '6')

total_max = int(s1) + int(s2)

if '6' in s1:
    s1 = s1.replace('6', '5')
if '6' in s2:
    s2 = s2.replace('6', '5')

total_min = int(s1) + int(s2)

print(total_min, total_max)