
# 고정점 찾기 다시 풀기

def binary_search(arr, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 고정점을 찾은 경우 인덱스 반환
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return binary_search(arr, start, mid - 1)
    # 중간점이 가리키는 위치의 값보다
    # 중간점이 큰 경우 오른쪽 확인
    else:
        return binary_search(arr, mid + 1, end)
    
n = 5
arr = [-15, -6, 1, 3, 7]

# 이진 탐색 수행
idx = binary_search(arr, 0, n - 1)

# 고정점이 없는 경우 -1 출력
if idx == None:
    print(-1)
else:
    print(idx)