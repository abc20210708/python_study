# 단어 뒤집기

## 참고 블로그
# https://art-coding3.tistory.com/40

import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    temp = list(input().split())
    for j in temp:
        print(j[::-1], end=' ')
        
##>> arr[::-1] # 처음부터 끝까지 -1칸 간격으로 
# ( == 역순으로)
##[9,8,7,6,5,4,3,2,1,0]

'''
import sys
 
n = int(sys.stdin.readline())
 
for _ in range(n):
    words = sys.stdin.readline().rstrip().split()

    for word in words:
        print(word[::-1], end=' ')
    print()
'''

'''
for _ in range(n):
    temp = input()
    temp += " "
    stack = []
    for i in temp:
        if i != " ":
            stack.append(i)
        else:
            while stack:
                print(stack.pop(), end='')
            print(' ', end='')
'''