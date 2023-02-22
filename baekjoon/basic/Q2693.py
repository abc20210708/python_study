# N번째 큰 수 

arr = []

for _ in range(int(input())):
    temp = (list(map(int, input().split())))
    temp.sort()
    arr.append(temp[-3])
    
for i in arr:
    print(i)