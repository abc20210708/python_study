## 수열 (실버 3) *

# 참고 블로그 https://sangminlog.tistory.com/entry/boj-2559
# https://m.blog.naver.com/repeater1384/222169483201
## https://my-coding-notes.tistory.com/489
n, k = map(int, input().split())
lst = list(map(int, input().split()))

tmp = sum(lst[:k])  
res = tmp

for i in range(k, n):
    tmp += lst[i] - lst[i-k]
    res = max(res, tmp)

print(res)




# 참고 블로그 https://velog.io/@yoonkeem/BOJ-2559%EB%B2%88-%EC%88%98%EC%97%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC
'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

part_sum = sum(lst[:k])
res = [part_sum]   

for i in range(len(lst)-k):
    print(part_sum)
    part_sum = part_sum - lst[i] + lst[i+k]
    res.append(part_sum)    

print(max(res))

'''

