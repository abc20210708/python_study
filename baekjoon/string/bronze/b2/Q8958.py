## OX퀴즈 (브론즈 2)
#  참고 블로그 https://codingpractices.tistory.com/entry/%EB%B0%B1%EC%A4%80-8958%EB%B2%88-OX%ED%80%B4%EC%A6%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python
t = int(input())

for _ in range(t):
    s = input()
    a = 0
    b = 0
    for i in s:
        if i == "O":
            b += 1
        else:
            b = 0
        a += b
    print(a)