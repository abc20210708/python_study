## 문자열 (실버 4)
#  참고 블로그 https://velog.io/@highcho/Algorithm-baekjoon-1120
import sys

a, b = map(str, sys.stdin.readline().strip().split())
ret = []
for i in range(len(b) - len(a) + 1): # a의 시작점을 변경하여 b문자열을 탐색할 수 있는 횟수
	cnt = 0
	for j in range(len(a)): # a 길이 만큼 전체
		if a[j] != b[i + j]: # b 문자열의 시작점을 변경해가며 a 전체 문장 탐색
			cnt += 1
	ret.append(cnt)
print(min(ret)) # 차이가 가장 적은 경우 선택