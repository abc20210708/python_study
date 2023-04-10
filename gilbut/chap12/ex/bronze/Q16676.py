## 근우의 다이어리 꾸미기 (브론즈 2) *

# 참고 블로그 https://data-make.tistory.com/404
n = input()
#n = "88"
s = '1' * len(n)

if len(n) == 1:
    print(1)
elif int(n) >= int(s):
    print(len(n))
else:
    print(len(n)-1)