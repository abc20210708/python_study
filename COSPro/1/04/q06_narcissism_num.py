## 문제6) 자아도취 수
#  참고 블로그 https://iwantbaobab.tistory.com/62

# base를 exponent만큼 제곱하여 반환
def power(base, exponent):
    val = 1
    for i in range(exponent):
        val *= base
    return val

def solution(k):
    res = []
    bound = power(10, k) # 영역 지정
    for i in range(bound // 10, bound): # k가 3인 경우 세 자리수 반복(100~999)
        current = i # 100~999 반복
        calc = 0 # current 숫자와 비교할 변수
        while current != 0:
            calc += power(current % 10, k) # 153 -> 3, 3 -> 27 -> ..
            # 각 자릿수별로 k 제곱 값을 누적
            current //= 10 # 153 -> 15 -> 1 -> 0
        if calc == i: # 두 수가 같으면
            res.append(i) # 자아도취 수 리스트에 추가
    return res




k = 3
ret = solution(k)

print("solution 함수의 반환 값은", ret, "입니다.")