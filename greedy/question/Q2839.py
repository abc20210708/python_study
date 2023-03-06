# 설탕 배달
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