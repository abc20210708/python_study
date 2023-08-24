## BABBA (실버 5)
#  참고 블로그 https://ywtechit.tistory.com/126

k = int(input())
n = 46
 
a = [0] * 46
a[0] = 1
a[1] = 0
 
b = [0] * 46
b[0] = 0
b[1] = 1
 
for i in range(2, n):
    a[i] = a[i - 1] + a[i - 2]
    b[i] = b[i - 1] + b[i - 2]
print(a[k], b[k])