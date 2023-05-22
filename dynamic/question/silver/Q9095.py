## 1, 2, 3 더하기 (실버 3) *
# 참고 블로그 https://e-you.tistory.com/304
d = [0] * 11
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 11):
    d[i] = d[i - 3] + d[i - 2] + d[i - 1]

n = int(input())
for _ in range(n):
    m = int(input())
    print(d[m])