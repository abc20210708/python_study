# 그대로 출력하기

while True:
    try:
        print(input())
    except EOFError: #(END OF FILE) 문자의 끝
        break
    

## 다른 풀이
try:
    while 1:
        print(input())
except:
    exit()

# 다른 풀이 2
# 참고 코드 https://www.acmicpc.net/source/54153013

import sys
print(sys.stdin.read())