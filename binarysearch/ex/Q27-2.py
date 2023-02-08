# 정렬된 배열에서 특정 수의 개수 구하기 (bisect)

from bisect import bisect_left, bisect_right

# 값이[left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_idx = bisect_right(array, right_value)
    left_idx = bisect_left(array, left_value)
    return right_idx - left_idx

n, x = map(int, input().split()) # 데이터의 개수 N , 찾고자 하는 값 x를 입력받기
array = list(map(int, input().split())) # 전체 데이터 입력받기

# 값이[x, x] 범위에 있는 데이터의 개수 계산
cnt = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if cnt == 0:
    print(-1)
else:
    print(cnt)
