## 이상한 곱셈 (브론즈 2)
#  참고 블로그 https://heewon9809.tistory.com/201
a, b = map(list, input().split())

a = list(map(int, a))
b = list(map(int, b))
print(sum(a)*sum(b))