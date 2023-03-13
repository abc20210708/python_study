# 동전 0

n, target = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.reverse()

# K원을 만드는데 필요한 동전 개수의 최솟값
cnt = 0

for i in arr:
    cnt += target // i
    target %= i
        
print(cnt)

