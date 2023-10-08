## 분수찾기 (실버 5)
#  참고 블로그 https://velog.io/@hrzo1617/%EB%B0%B1%EC%A4%80-1193-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B6%84%EC%88%98%EC%B0%BE%EA%B8%B0

n = int(input())
line = 1

while n > line:
    n -= line
    line += 1

if line % 2 == 0:
    up = n
    down = line - n + 1
else:
    up = line - n + 1
    down = n

print(up, '/', down, sep="")