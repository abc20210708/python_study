# 1이 될 때까지

'''
1. N에서 1을 뺀다.
2. N을 K로 나눈다.
'''

n, k = map(int, input().split())
#n, k = 27, 3
result = 0

while True:
    #(N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k # K의 배수로 만들기
    result += (n - target) # K의 배수로 만들기까지의 -1 횟수 더하기
    n = target
    
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    
    # K로 나누기
    result += 1
    n //= k


# 마지막으로 남은 수에 대하여 1씩 빼기
# n이 k보다 작아졌을 때는 계속 -1해서 1로 만들기
result += (n - 1)
print(result)

'''
이 코드에서 result += (n - 1)은 마지막으로 남은 수 n을 
1로 만들기 위해 1을 뺀 횟수를 result에 더하는 부분입니다.

반복문을 통해 n을 K로 나눌 수 없을 때까지 계속해서 1을 뺀 후, 
K로 나누고 있습니다. 이 때, n이 K보다 작아지면 더 이상 나눌 수 
없으므로 반복문을 탈출합니다. 

그러나 n이 K보다 작아졌을 때에도 n을 1로 만들기 위해 
1을 뺀 횟수를 추가해야 합니다.

예를 들어, n이 2이고 k가 3인 경우를 생각해봅시다. 처
음에 n에서 1을 빼면 1이 되고, 이후에는 더 이상 3으로 
나눌 수 없으므로 반복문을 탈출합니다. 

그러나 n이 1이 되려면 1을 더 빼야 하므로 result에 1을 더해주는 것입니다.
따라서 result += (n - 1)은 마지막으로 남은 수 n을 1로 만들기 위해 1을 뺀 횟수를 
result에 추가하는 역할을 합니다.

'''

'''
# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1
        
# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1
'''