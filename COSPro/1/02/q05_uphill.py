## 문제5) 언제까지 오르막길이야..?!
#  참고 블로그 https://velog.io/@corone_hi/COS-PRO-1%EA%B8%89-2%EC%B0%A8-%EB%AC%B8%EC%A0%9C5-%EC%96%B8%EC%A0%9C%EA%B9%8C%EC%A7%80-%EC%98%A4%EB%A5%B4%EB%A7%89%EA%B8%B8%EC%9D%B4%EC%95%BC


def solution(arr):
	answer = 0
	
	prev = arr[0]
	cnt = 1
	
	for i in range(len(arr)):
		if arr[i] > prev:
			cnt += 1
		else:
			answer = max(answer, cnt)
			cnt = 1
			
		prev = arr[i]
	
	return answer

arr = [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]
ret = solution(arr)

print("solution 함수의 반환 값은", ret, "입니다.")