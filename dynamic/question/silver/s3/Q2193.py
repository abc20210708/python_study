## 이친수 (실버 3)

n = int(input())

if n <= 2:
    print(1)
else:
    lst = [0, 1, 1]
    for i in range(3, n+1):
        lst.append(lst[i-1] + lst[i-2])
    print(lst[n])

'''
예를 들면 1, 10, 100, 101, 1000, 1001 등이 이친수가 된다는
본문의 설명에서 4자리일 때는 1000, 1001, 1010으로 총 3개

1 - 1, 2 - 1, 3 - 2, 4 - 3
'''