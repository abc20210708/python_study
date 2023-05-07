## 기타줄 (실버 4)

# 참고 코드 https://www.acmicpc.net/source/54478306
N, M = map(int,input().split())
arr_6 = []
arr_1 = []

for _ in range(M):
    a, b = map(int,input().split())
    arr_6.append(a)
    arr_1.append(b)

arr_6.sort()
arr_1.sort()

print(min(arr_1[0]*N, arr_6[0]*(N//6)+arr_1[0]*(N%6), arr_6[0]*(N//6+1)))


# 내가 작성한 코드
n, m = map(int, input().split())

a = []
for i in range(m):
    x, y = map(int, input().split())
    a.append([x, y])
    
a.sort(key=lambda x:x[0])
b = a.copy()
b.sort(key=lambda x:x[1])

n1 = n2 = n3= 0
n1 = n // 6
if n % 6 != 0 : n1 += 1
n1 = (a[0][0] * n1)
n2 = (b[0][1] * n)
n3 = (a[0][0] * (n//6)) + (b[0][1] * (n%6))

print(min(n1, n2, n3))