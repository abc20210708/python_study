## 문제10) 사과 박스 무게의 불량 검사
#  참고 블로그 https://popooly.tistory.com/277?category=1073615



def solution(weight, boxes):
	answer = 0
	for x in boxes:
     # if weight - (weight * 0.1) > x or weight + (weight * 0.1) < x:
		if weight  * 0.9 > x or weight  * 1.1 < x:
			answer += 1
	return answer

weight = 600
boxes = [653, 670, 533, 540, 660]
ret = solution(weight, boxes)

print("solution 함수의 반환 값은", ret, "입니다.")