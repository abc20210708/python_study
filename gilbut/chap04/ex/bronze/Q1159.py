## 농구 경기 (브론즈 2)

li = sorted([input()[0] for _ in range(int(input()))])
s = set(li)
res = []

for c in s:
    if li.count(c) >= 5:
        res.append(c)

print(''.join(sorted(res)) if len(res) > 0 else "PREDAJA")




n = int(input())
arr = [0] * 26

for i in range(n):
    s = input()
    arr[(ord(s[0]))-97] += 1
    

if max(arr) < 5:
    print("PREDAJA")
    
for i in range(len(arr)):
    if arr[i] >= 5:
        print(chr(i+97), end="")
