## 동일한 단어 그룹화하기 (실버 4)
# 다른 풀이 #
import sys
input = sys.stdin.readline

n = int(input())
dic = dict()
for _ in range(n):
    s = list(input().rstrip())
    s = sorted(s)
    s = ''.join(s)
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1
        
print(len(dic))


#  참고 블로그 https://ye5ni.tistory.com/64

n = int(input())

res = []
for _ in range(n):
    s = sorted(list(input()))
    s = ''.join(s)
    if s not in res:
        res.append(s)

print(len(res))
    