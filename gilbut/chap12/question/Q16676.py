## 근우의 다이어리 꾸미기 (브론즈 2) *

n = input()
s = '1' * len(n)

if len(n) == 1:
    print(1)
elif int(n) >= int(s):
    print(len(n))
else:
    print(len(n)-1)