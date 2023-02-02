
# 1이 될 때까지 다시 풀어보기

'''

'''

n, k = 27, 3

result = 0


while True :
    target = (n // k) * 3
    result += (n - target)
    n = target
    
    if n < k:
        break
    
    # K로 나누기
    result += 1
    n //= k

# n이 k보다 작아졌을 때는 계속 -1해서 1로 만들기
result += (n -1)
print(result)






