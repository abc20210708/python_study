
# 숫자 카드 게임 다시 풀기

# 카드들이 n * m 형태

n, m = 2, 4

arr = [
    [7, 3, 1, 8],
    [3, 3, 3, 4]
]

result = 0

for i in range(n):
    min_val = min(arr[i])
    # 현재 줄에서 가장 작은 수
    result = max(result, min_val)

print(result)