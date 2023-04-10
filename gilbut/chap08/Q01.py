# 이진 탐색 구현 방법

# low와 high 변수를 사용해 원하는 값이 어디인지 파악하는 것이 핵심
def bisect(a, x, lo= 0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

my_list = [1, 2, 3, 7, 9, 11, 33]
print(bisect(my_list, 3))