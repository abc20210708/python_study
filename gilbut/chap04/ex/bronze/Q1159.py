## 농구 경기 (브론즈 2)

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
