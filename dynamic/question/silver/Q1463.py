## 1로 만들기 (실버 3) *
# 참고 블로그 https://bio-info.tistory.com/159

target = int(input())
d = [0] * (target + 1)

for i in range(2, target + 1):
    d[i] = d[i - 1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)

print(d[target])