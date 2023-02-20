## 참고 블로그 https://covenant.tistory.com/141

# 1-1. 나누어 입력받기
a, b =  map(int, input().split())


# 1-2. 입력 출력 가속
import sys
N = int(sys.stdin.readline())

# print 함수와 다르게 문자열일 경우만 출력 가능
sys.stdout.write(str(N))

# 입력 출력 더 간단히
from sys import stdin, stdout
input = stdin.readline
print = stdout.write


