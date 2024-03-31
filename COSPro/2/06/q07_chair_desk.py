## 문제7) 의자와 책상을 사고싶어요.
#  참고 블로그 https://popooly.tistory.com/274?category=1073615


def solution(money, chairs, desks):
    answer = 0
    for chair in chairs:
        for desk in desks:
            price = chair + desk
            if answer < price and price <= money:
                answer = price
    return answer

money1 = 7
chairs1 = [2, 5]
desks1 = [4, 3, 5]
ret1 = solution(money1, chairs1, desks1)

print("solution 함수의 반환 값은", ret1, "입니다.")