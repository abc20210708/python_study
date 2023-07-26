## 연속합 (실버 2) *
# 참고 블로그 https://wook-2124.tistory.com/406

n = int(input())
lst = list(map(int, input().split()))

for i in range(1, n):
    lst[i] = max(lst[i], lst[i-1] + lst[i])

print(max(lst))