## 주사위 게임 (브론즈 2)
#  참고 블로그 https://uknowblog.tistory.com/69

n, m = map(int, input().split())

lst = []
res = 0

# n개의 숫자 리스트 
for _ in range(n):
    lst.append(int(input()))
    
# 주사위 던지기

for i in range(1, n):
   
   res += int(input())
   
   if res >= n -1 :
       print(i)
       break
   
   res += lst[res]
   
   if res >= n-1:
       print(i)
       break
    