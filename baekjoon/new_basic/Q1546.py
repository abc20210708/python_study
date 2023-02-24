# 평균

n = int(input())
arr = list(map(int, input().split()))

max_val = max(arr)

total = 0
for i in arr:
    total += (i / max_val * 100)
    
print(total / n)