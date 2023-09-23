## 올림픽 (실버 5)
#  참고 블로그 https://develop247.tistory.com/234

n, k = map(int, input().split())

medals = [list(map(int, input().split())) for _ in range(n)]

medals = sorted(medals, key=lambda x: (-x[1], -x[2], -x[3]))
# 또는 medals.sort(key = lambda x: (x[1], x[2], x[3]), reverse=True)

idx = [medals[i][0] for i in range(n)].index(k)

for i in range(n):
    if medals[idx][1:] == medals[i][1:]:
        print(i+1)
        break

'''
나의 풀이

n, k = map(int, input().split())

lst = []

for j in range(n):
    arr = list(map(int, input().split()))
    lst.append(arr)

lst = sorted(lst, key=lambda x: [-x[1], -x[2], -x[3]])
'''

