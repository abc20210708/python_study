# 크로아티아 알파벳

n = "ljes=njak"
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in cro:
    n = n.replace(i, 'a')

print(len(n))

## 참고 블로그 https://one-hour.tistory.com/25