# 고정점 찾기

# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 고정점을 찾은 경우 인덱스 반환
    if array[mid] == mid:
        return mid
    # 중간점이 가리키는 위치의 값보다 중간점이 작은 경우 왼쪽 확인
    elif array[mid] > mid:
        return binary_search(array, start, mid -1)
    # 중간점이 가리키는 위치의 값보다 중간점이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, mid + 1, end)
    
#n = int(input())
n = 5
#array = list(map(int, input().split()))
array = [-15, -6, 1, 3, 7]

# 이진 탐색 수행
idx = binary_search(array, 0, n - 1)

# 고정점이 없는 경우 -1 출력
if idx == None:
    print(-1)
# 고정점이 있는 경우 해당 인덱스 출력
else: 
    print(idx)
        