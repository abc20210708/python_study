## 적어도 대부분의 배수 (브론즈 1)
#  참고 블로그 https://velog.io/@poiu0329/%EB%B0%B1%EC%A4%80-1145%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A0%81%EC%96%B4%EB%8F%84-%EB%8C%80%EB%B6%80%EB%B6%84%EC%9D%98-%EB%B0%B0%EC%88%98

a = list(map(int, input().split()))
min = min(a)   # 최솟값을 찾은 뒤
while True:
    cnt = 0
    for i in a:
        if min % i == 0:   # 배수를 찾는 반복문
            cnt += 1
    if cnt > 2:   # 3개를 찾았다면 break
        break
    min += 1   # 3개를 찾을때까지 값을 올려준다.
print(min)