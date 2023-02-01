# 일단 입력값 중에서 가장 큰 수와 두 번째로 큰 수만 저장
# 연속으로 더할 수 있는 횟수는 최대 K번이므로
# 가장 큰 수를 K번 더하고, 두 번째로 큰 수를 한 번 더하는 연산 반복

# N, M, K를 공백으로 구분해 입력받기
n, m, k= map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정리하기
first = data[n- 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

result = 0

# 가장 큰 수가 더해지는 횟수 계산
cnt = int(m / (k + 1)) * k
cnt += m % (k + 1)


result += (cnt) * first # 가장 큰 수 더하기
result += (m - cnt) * second # 두 번째로 큰 수 더하기

print(result)

'''
 m / (k + 1) 수열이 반복되는 횟수
 수열 반복되는 횟수에 K를 곱하면 
 가장 큰 수(first)가 등장하는 횟수
 
 이때 M이 (K + 1)로 나누어덜어지지 않는 경우도 고려
 그럴 때는 M을 (K+1)로 나눈 나머지만큼 가장 큰 수가
 추가로 더해지마를 이를 고려해 주어야 한다.
 
'''
        
        
'''
while True:
    for i in range(k) : # 가장 큰 수를 K번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할 때마다 1씩 빼기
    if m == 0: # m이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 #더할 때마다 1씩 빼기
    
print(result) #최종 답안 출력
'''