# 효율적인 화폐 구성

n, m = 3, 7
arr = [
    2,
    3,
    5
]

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1) # m원 + 1 크기만큼 

# 다이나믹 프로그래밍 진행
d[0] = 0
for i in range(n):
    for j in range(arr[i], m + 1):
        if d[j - arr[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            print("arr[i]",arr[i])
            d[j] = min(d[j], d[j - arr[i]] + 1)
            

# 계산된 결과 출력
if d[m] == 10001: # 방법이 없는 경우
    print(-1)
else:
    print(d[m])
