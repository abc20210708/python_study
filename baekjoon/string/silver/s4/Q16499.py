## 동일한 단어 그룹화하기 (실버 4)
#  참고 블로그 https://ye5ni.tistory.com/64

n = int(input())

res = []
for _ in range(n):
    s = sorted(list(input()))
    s = ''.join(s)
    if s not in res:
        res.append(s)

print(len(res))
    