## 색종이 (실버 5)
#  참고 블로그 https://velog.io/@zinu/%EB%B0%B1%EC%A4%80-2563-%EC%83%89%EC%A2%85%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-2%EC%B0%A8%EC%9B%90%EB%B0%B0%EC%97%B4

n = int(input())
arr = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y = list(map(int, input().split()))
    
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1
            
res = 0

for i in arr:
    res += i.count(1)
print(res)
'''
for i in range(20):
    for j in range(20):
        print(arr[i][j], end=' ')
    print()
'''