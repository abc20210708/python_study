## 컴홀더 (브론즈 1)
#  참고 블로그 https://s0ng.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EA%B7%B8%EB%A6%AC%EB%94%94-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%BB%B5%ED%99%80%EB%8D%94-2810%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python

n = int(input())
s = input().rstrip()

cnt = s.count('LL')

if cnt <= 1:
    print(len(s))
else:
    print(len(s) - cnt + 1)