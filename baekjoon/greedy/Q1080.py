## 행렬 (실버 1) *

a, b = map(int, input().split())
cnt = 0

A = [list(map(int, input())) for _ in range(a)]
B = [list(map(int, input())) for _ in range(a)]

def solution(x, y, A):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 - A[i][j]
            
for i in range(a-2):
    for j in range(b-2):
        if A[i][j] != B[i][j]:
            solution(i, j, A)
            cnt += 1

flag = True
for i in range(a):
    for j in range(b):
        if A[i][j] != B[i][j]:
            flag = False
            break

print(cnt) if flag else print(-1)