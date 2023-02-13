# 개미 전사

n = 4
arr = [1, 3, 1, 5]

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍 진행(보텀업)
d[0] = arr[0]
d[1] = max(arr[0], arr[1])
for i in  range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + arr[i])
    
# 계산된 결과 출력
print(d[n - 1])
