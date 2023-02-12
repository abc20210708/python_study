
# 이진 탐색(재귀 함수) 다시 풀기

def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid -1)
    else:
        return binary_search(arr, target, mid + 1, end)
    
n, target = 10, 7
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 이진 탐색 결과 출력
result = binary_search(arr, target, 0, n -1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
    