n = int(input())
w = []
res = 0

for i in range(n):
    w.append(int(input()))
    
w.sort()

for i in range(len(w)):
    if w[i] * n > res:
        res = w[i] * n
    n -= 1
    
print(res)