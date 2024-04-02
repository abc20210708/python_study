## 문제6) 체스의 나이트
#  참고 블로그 https://iwantbaobab.tistory.com/28

def solution(pos):
	answer = 0
	
	x = ord(pos[0]) - ord('A')
	y = ord(pos[1]) - ord('1')
	
	dx = [2, 1, -1, -2, -2, -1, 1, 2]
	dy = [1, 2, 2, 1, -1, -2, -2, -1]
	
	for i in range(8):
		nx = x + dx[i]
		ny = y + dy[i]
		
		if nx >= 0 and nx < 8 and ny >= 0 and ny < 8:
			answer += 1

	return answer


pos = "A7"
ret = solution(pos)

print("solution 함수의 반환 값은", ret, "입니다.")