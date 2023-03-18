import math

# M과 N을 입력받기
#m, n = map(int, input().split())
m, n = 3, 16
# 처음에는 모든 수가 소수(True)인 것으로 초기화
arr = [True] * 100

for i in range(2, int(math.sqrt(n))+1):
    if arr[i] == True:
        j = 2
        while i * j <= n:
            arr[i*j] = False
            j += 1 
            
for i in range(m, n + 1):
    if arr[i]:
        print(i)

