## 좌표 정렬하기 (실버 5)

lst = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    lst.append([x, y])

lst.sort(key=lambda x:(x[0], x[1]))

for i,j in lst:
    print(i, j)