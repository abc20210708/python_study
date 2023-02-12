# 선택 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

'''
배열 안의 자료 중 가장 작은 수를 찾아 선택해 놓은 다음,
순서대로 교체하는 방식의 정렬
'''


for i in range(len(array)):
    min_idx = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i] # 스와프
    
print(array)

# 0 인덱스와 1 인덱스의 원소 교체하기
array1 = [3, 5]  
array1[0], array1[1] = array1[1], array1[0]

print(array1)

