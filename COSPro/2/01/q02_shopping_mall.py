##  문제2) 쇼핑몰 등급별 할인 금액구하기

def solution(price, grade):
	answer = 0
	
	if grade == 'V':
		answer = price * 0.15
	elif grade == 'G':
		answer = price * 0.10
	else:
		answer = price * 0.05
	
	return int(price - answer)