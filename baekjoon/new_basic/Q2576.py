# 홀수

arr = []
for i in range(7):
    num = int(input())
    if num % 2 == 1:
        arr.append(num)
        
arr.sort()

if len(arr) < 1:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))
    