## 더하기 사이클 (브론즈 1)
#  참고 블로그 https://wook-2124.tistory.com/222

n = int(input())
num = n
cnt = 0

while 1:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c
    
    cnt = cnt + 1
    if (num == n):
        break
    
print(cnt) 