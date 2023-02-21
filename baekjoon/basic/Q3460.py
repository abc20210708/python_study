# 이진수

# 참고 블로그 https://leejunggae.tistory.com/98

def binary(n):
    i = 0
    while n != 0:
        if n % 2 == 1:
            print(i, end=" ")
        n //= 2
        i += 1
        
for _ in range(int(input())):
    binary(int(input()))
