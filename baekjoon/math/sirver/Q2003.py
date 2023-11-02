## 수들의 합 (실버 4)
#  참고 블로그 https://my-coding-notes.tistory.com/225

n, m = map(int, input().split())
a = list(map(int, input().split()))

i, j, cnt, total = 0, 0, 0, 0

while 1:
    if total >= m:
        i += 1
        total -= a[i]
    elif j == n:
        break
    else:
        j += 1
        total += a[j]
    
    if total == m:
        cnt += 1

print(cnt)
