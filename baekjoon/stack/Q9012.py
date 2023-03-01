# 괄호
# 참고 블로그
# https://wook-2124.tistory.com/442
import sys
input = sys.stdin.readline




n = int(input())

for _ in range(n):
    stack = []
    temp = list(input())
    cnt = 0
    
    for i in temp:
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1
        if cnt < 0:
            print("NO")
            break
    
    if cnt > 0:
        print("NO")
    elif cnt == 0:
        print("YES")
       