## BABBA (실버 5)

# 참고 블로그 https://bio-info.tistory.com/217

K = int(input()) # 버튼을 누른 횟수 K
a, b = 0, 1 # 버튼을 1번 누른 경우로 초기화

for i in range(1,K): # 2번 누른것부터 for문 반복
    a,b = b,a+b # 피보나치 수열 진행
    
print(a,b) # A개수, B개수 출력


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