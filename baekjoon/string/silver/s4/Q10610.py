## 30 (실버 4)
#  참고 블로그 https://jae04099.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%92%80%EC%9D%B4-%EB%B0%B1%EC%A4%80-10610-30
n = input()

n = sorted(n, reverse=True)

total = 0

if '0' not in n:
    print(-1)
else:
    for i in n:
        total += int(i)
    if total % 3 != 0:
        print(-1)
    else:
        print(''.join(n))