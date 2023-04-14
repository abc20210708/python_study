# 농구 경기 다시 풀기

n = int(input())

arr = []
for i in range(n):
    arr.append(input()[0])
    
res = []
s = set(arr)

for i in s:
    if arr.count(i) >= 5:
        res.append(i)
        
res.sort()

if len(res) == 0:
    print("PREDAJA")
else:
    print(''.join(res))