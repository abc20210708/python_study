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