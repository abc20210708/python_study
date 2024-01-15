## 0의 개수 (브론즈 1)
#  참고 블로그 https://oort-cloud.tistory.com/entry/%EB%B0%B1%EC%A4%80-11170%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%ACpython-0%EC%9D%98-%EA%B0%9C%EC%88%98

x = int(input())
for i in range(x):
    count = 0
    a, b = map(int, input().split())
    for i in range(a, b+1):
        w = str(i)
        count += w.count('0')
    print(count)