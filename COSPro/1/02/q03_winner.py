## 문제3) 경품 당첨자를 구해주세요.
#  참고 블로그 https://velog.io/@corone_hi/COS-PRO-1%EA%B8%89-2%EC%B0%A8-%EB%AC%B8%EC%A0%9C3-%EA%B2%BD%ED%92%88-%EB%8B%B9%EC%B2%A8%EC%9E%90%EB%A5%BC-%EA%B5%AC%ED%95%B4%EC%A3%BC%EC%84%B8%EC%9A%94

def func_a(n):
	ret = 1
	while n > 0:
		ret *= 10
		n -= 1
	return ret

def func_b(n):
	ret = 0
	while n > 0:
		ret += 1
		n //= 10
	return ret

def func_c(n):
	ret = 0
	while n > 0:
		ret += n%10
		n //= 10
	return ret


def solution(num):
	next_num = num
	while True:
		next_num += 1
		length = func_b(next_num)
		if length % 2 != 0:
			continue
		divisor = func_a(length//2)  
		front = next_num // divisor
		back = next_num % divisor

		front_sum = func_c(front)
		back_sum = func_c(back)
		if front_sum == back_sum:
			break
	return next_num - num
            


num1 = 1
ret1 = solution(num1)

print("solution 함수의 반환 값은", ret1, "입니다.")

num2 = 235386
ret2 = solution(num2)

print("solution 함수의 반환 값은", ret2, "입니다.")