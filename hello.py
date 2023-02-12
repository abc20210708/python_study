
# 정렬된 배열에서 특정 수의 개수 구하기 (bisect) 다시 풀기

from bisect import bisect_left, bisect_right

# 값이[left_value, right_value]인 데이터의 개수
def cnt_by_range(arr, left_val, right_val):
    right_idx = bisect_right(arr, right_val)
    left_idx = bisect_left(arr, left_val)
    return right_idx - left_idx

n, x = 7, 2
arr = [1, 1, 2, 2, 2, 2, 3]

cnt = cnt_by_range(arr, x, x)

# 값이 x인 원소가 존재하지 않는다면
if cnt == 0:
    print(-1)
else:
    print(cnt)