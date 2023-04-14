# 명령 프롬프트 다시 풀기

n = int(input())
arr = list(input())


for i in range(n - 1):
    temp = list(input())
    for j in range(len(arr)):
        if arr[j] != temp[j]:
            arr[j] = "?"
            
print(''.join(arr))