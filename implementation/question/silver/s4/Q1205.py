## 등수 구하기 (실버 4)
#  참고 블로그 https://sodehdt-ldkt.tistory.com/217

n, tmp, p = map(int, input().split())

if n == 0:
    print(1)
else:
    rank = list(map(int, input().split()))
    
    if n == p and rank[-1] >= tmp:
        print(-1)
    else:
        res = n+1
        for i in range(n):
            if rank[i] <= tmp:
                res = i+1
                break
        print(res)