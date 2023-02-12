# 삽입 정렬
# 참고 블로그 https://computer-science-student.tistory.com/559

'''
모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교해,
자신의 위치를 찾아 삽임함으로써 정렬을 완성하는 알고리즘
'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): #인덱스 i부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
            #print(array)
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
        
print("최종 삽입 정렬 : ")
print(array)


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j]   = arr[j], arr[j - 1]
            j -= 1
    return arr

print(insertion_sort(arr))