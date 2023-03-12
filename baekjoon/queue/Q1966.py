# 프린터 큐

n = int(input())
for i in range(n):
    m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    while len(arr) > 0:
        if arr[0] == max(arr):
            cnt += 1
            arr.pop(0)
            if k == 0: break
        else:
            arr.append(arr.pop(0))
        k = k - 1 if k > 0 else len(arr) -1
    print(cnt)
            
        
        
    