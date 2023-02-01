# N, M 공백으로 입력받기
n, m = map(int, input().split())

result = 0

# 한 줄씩 입력 받아 확인
for i in range(n) :
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수' 중에서 큰 수 찾기
    result = max(min_value, result)
    
print(result)


'''
# 2중 반복문 구조를 이용
# 한 줄씩 입력받아 확인
for i in range(n) :
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data :
        min_value = min(a, min_value)
    #'가장 작은 수' 중에서 가장 큰 수 찾기
    result = max(result, min_value)
    
print(result)
'''