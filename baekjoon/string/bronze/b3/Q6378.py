## 디지털 루트 (브론즈 3)
#  참고 블로그 https://jinho-study.tistory.com/151

while 1:
    n = int(input())
    if n :
        while n > 9:
            n = sum(map(int, list(str(n))))
        print(n)
    else:
        break
## ** 모든 자릿수의 합을 구해줌
## sum(map(int, list(str(n)))) 