## 피자 small (실버 5)
#  참고 블로그 https://jinho-study.tistory.com/971


import sys
input = sys.stdin.readline

n = int(input()) # 피자판의 개수

if n == 1:
    print(0)
    exit()
    
print(n * (n-1) // 2)