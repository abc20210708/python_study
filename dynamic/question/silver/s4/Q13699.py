## 점화식 (실버 4)

## 다른 풀이
#  참고 블로그 https://kau-algorithm.tistory.com/441

n = int(input())
d = [0] * 36

d[0] = 1
d[1] = 1
d[2] = 2
d[3] = 5

if n > 3:
    for i in range(4, n+1):
        for j in range(i):
            d[i] += d[j] * d[i-j-1]

print(d[n])

'''
틀린 내가 작성한 풀이
n = int(input())

d = [1, 1, 2, 5]

if n <= 3:
    print(d[n])
else:
    for i in range(4, n+1):
        d.append((d[i-1]*2)+(d[i-2]*2))
    print(d[n])
'''    