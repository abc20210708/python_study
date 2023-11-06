## 블로그 (실버 3)
#  참고 블로그 https://velog.io/@7rgoong/BOJ-21921.-%EB%B8%94%EB%A1%9C%EA%B7%B8
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
lst = list(map(int, input().split()))


if max(lst) == 0:
    print("SAD")
else:
    lst_max = sum(lst[:x])
    tmp = lst_max
    cnt = 1
    
    for i in range(x, n):
        tmp -= lst[i-x]
        tmp += lst[i]
        
        if tmp > lst_max:
            lst_max = tmp
            cnt = 1
        elif tmp == lst_max:
            cnt += 1
    print(lst_max)
    print(cnt)
            