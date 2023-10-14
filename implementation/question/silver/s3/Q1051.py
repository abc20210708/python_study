## 숫자 정사각형 (실버 3)

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

res = []
tmp = min(n, m)

for i in range(n):
    for j in range(m):
        for k in range(tmp):
            if ((i+k)<n) and (j+k<m):
                if (arr[i][j] == arr[i+k][j] == arr[i][j+k] == arr[i+k][j+k]):
                    res.append((k+1)**2)  
print(max(res))