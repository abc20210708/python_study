##  문제9) 위험한 지역 몇개인지 알려주기
#   참고 블로그 https://velog.io/@brown_eyed87/220925TIL-COS-PRO-2%EA%B8%89-Python-4%EC%B0%A8-%EB%AC%B8%EC%A0%9C9-%EC%9C%84%ED%97%98%ED%95%9C-%EC%A7%80%EC%97%AD-%EB%AA%87%EA%B0%9C%EC%9D%B8%EC%A7%80-%EC%95%8C%EB%A0%A4%EC%A3%BC%EA%B8%B0
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def chk(i, j):
	if i > 0 and height[i][j] > height[i-1][j]:
		pass
	elif i < 3 and height[i][j] > height[i+1][j]:
		pass
	elif j > 0 and height[i][j] > height[i][j-1]:
		pass
	elif j < 3 and height[i][j] > height[i][j+1]:
		pass
	else:
		return 1
	return 0
	

def solution(height):
	cnt = 0
	for i in range(4):
		for j in range(4):
			#chk() 통해 확인한 값을 추가
			cnt += chk(i,j)
	return cnt


height = [[3, 6, 2, 8], [7, 3, 4, 2], [8, 6, 7, 3], [5, 3, 2, 9]]
ret = solution(height)

print("solution 함수의 반환 값은", ret, "입니다.")