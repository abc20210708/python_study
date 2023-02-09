
# 1이 될 때까지 효율적으로 다시 풀기

'''

'''
n, k = 25, 3
result = 0

while True:
    # (N == K 로 나우어 떨어지는 수)가 될 떄까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    
    # N이 K보다 작을 때(더 이상 나울 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k
    
# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
    
print(result)
        
    


