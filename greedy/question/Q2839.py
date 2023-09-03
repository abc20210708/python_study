# 설탕 배달 (실버 4)

## 참고 블로그 https://jobdong7757.tistory.com/33

n = int(input())

d = [10001] * 5001
d[0] = 0

for i in range(3, n+1):
    if i-5 >= 0 and d[i-5] != 10001:
        d[i] = min(d[i], d[i-5]+1)
    if d[i-3] != 10001:
        d[i] = min(d[i], d[i-3]+1)

if d[n] == 10001:
    print(-1)
else:
    print(d[n])



## 참고 블로그 https://ooyoung.tistory.com/81

sugar = int(input())

bag = 0
while sugar >= 0:
    if sugar % 5 == 0: # 5의 배수라면
        bag += (sugar // 5)
        print(bag)
        break
    sugar -= 3
    bag += 1 # 5의 배수가 될 때까지 설탕 -3, 봉지 + 1
else: # sugar 변수가 0보다 작아지면 else문으로 내려옴
    print(-1)