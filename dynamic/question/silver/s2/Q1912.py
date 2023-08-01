## 연속합 (실버 2) *
# 참고 블로그 https://wook-2124.tistory.com/406

# 입력값으로 수열의 길이 n을 받습니다.
n = int(input())

# 입력값으로 n개의 정수를 받아서 리스트 lst에 저장합니다.
lst = list(map(int, input().split()))

# lst[i]는 i번째 원소까지의 연속된 부분 수열의 합 중에서 가장 큰 값을 나타냅니다.
# lst[i]의 값을 갱신하면서, i번째 원소까지의 연속된 부분 수열의 합 중 가장 큰 값을 계속 업데이트합니다.
for i in range(1, n):
    lst[i] = max(lst[i], lst[i-1] + lst[i])

# lst 리스트에서 가장 큰 값을 출력하면 문제에서 요구하는 최대 연속합을 구할 수 있습니다.
print(max(lst))
