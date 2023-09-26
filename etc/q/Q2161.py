## 카드1 (실버 5)

# 1~ n
n = int(input())

d = []

for i in range(1, n+1):
    d.append(i)

while len(d) != 1:
    print(d.pop(0), end=" ") # 2, 3, 4
    d.append(d.pop(0)) # 3, 4, 2
    print(d.pop(0), end=" ") # 4, 2

print(d[0], end=" ")
    
    