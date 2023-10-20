## 좌표 정렬하기 (실버 5)
import sys
input = sys.stdin.readline

lst = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    lst.append([x, y])

lst.sort(key=lambda x:(x[0], x[1]))

for i,j in lst:
    print(i, j)

'''
import sys
input = sys.stdin.readline
코드 추가로
4416ms -> 348ms 시간 단축
'''