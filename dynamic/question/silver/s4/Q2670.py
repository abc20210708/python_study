## 연속 부분 최대곱 (실버 4)
#  참고 블로그 https://velog.io/@deannn/BOJ-%EB%B0%B1%EC%A4%80-2670%EB%B2%88-%EC%97%B0%EC%86%8D%EB%B6%80%EB%B6%84%EC%B5%9C%EB%8C%80%EA%B3%B1-Python

N = int(input())
arr = list(float(input()) for _ in range(N))
for i in range(1, N):
    arr[i] = max(arr[i], arr[i] * arr[i - 1])
print('%0.3f' % max(arr))