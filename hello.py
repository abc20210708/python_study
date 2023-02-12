
# 삽입 정렬 다시 풀기


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): #인덱스i부터 1까지 -1씩 감소
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break
        
print("최종 삽입 정렬 : ")
print(array)


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j - 1]  > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1] 
            j -= 1
    return arr


print(insertion_sort(arr))



