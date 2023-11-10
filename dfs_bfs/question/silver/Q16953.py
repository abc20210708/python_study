## A → B (실버 2)
#  참고 블로그 https://my-coding-notes.tistory.com/210

a, b = map(int, input().split())
tmp = 1

while b != a:
    tmp += 1
    num = b
    
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    
    if num == b:
        print(-1)
        break
else:
    print(tmp)