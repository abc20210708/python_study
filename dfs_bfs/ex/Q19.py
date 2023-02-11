# 연산자 끼워 넣기

n = 3

# 연산을 수행하고자 하는 수 리스트
data = [3, 4, 5]
# 더하기, 빼기, 곱하기, 나누기 연산자의 개수
add, sub, mul, div = 1, 0, 1, 0

# 최솟값과 최댓값 초기화
min_val = 1e9
max_val = -1e9

# 깊이 우선 탐색 메서드
def dfs(i, now):
    global min_val, max_val, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_val = min(min_val, now)
        max_val = max(max_val, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, now / data[i]) # 나눌 때는 나머지를 제거
            div += 1
            
# DFS 메서드 호출
dfs(1, data[0])

# 최댓값과 최솟값 차례대로 출력
print(max_val)
print(min_val)