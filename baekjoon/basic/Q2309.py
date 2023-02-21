# 일곱 난쟁이


arr = []

for _ in range(9):
    arr.append(int(input()))

temp = sum(arr)


for i in range(8):
    for j in range(i + 1, 9):
        if temp - (arr[i] + arr[j]) == 100:
            num1 = arr[i]
            num2 = arr[j]
            
arr.remove(num1)
arr.remove(num2)
arr.sort()


for i in arr:
    print(i)    

