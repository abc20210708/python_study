## LCS (골드 5) *

# 참고 블로그 https://myjamong.tistory.com/317
import sys

input = sys.stdin.readline

# 입력받은 두 문자열을 공백 제거하여 s1, s2에 저장
s1, s2 = input().strip(), input().strip() 
# s1과 s2의 길이를 저장
l1, l2 = len(s1), len(s2) 

# l2 길이만큼의 0으로 채워진 리스트 cache를 생성. 
# LCS의 길이를 저장할 예정
cache = [0] * l2 

# 첫 번째 문자열인 s1을 한 글자씩 순회
for i in range(l1): 
    cnt = 0 # 현재 글자에서의 LCS의 길이를 저장할 변수
    # 두 번째 문자열인 s2를 한 글자씩 순회
    for j in range(l2): 
        # 현재까지의 LCS의 길이보다 
        # cache[j]가 더 크다면, cnt를 업데이트
        if cnt < cache[j]: 
            cnt = cache[j]
        # s1[i]와 s2[j]가 같다면, 
        # 새로운 문자가 LCS에 포함되는 것이므로 cnt를 1 증가
        elif s1[i] == s2[j]: 
            # cache[j]에 cnt + 1을 저장하여 
            # 새로운 LCS의 길이를 업데이트
            cache[j] = cnt + 1 

# 최종적으로 cache에 저장된 값들 중 가장 큰 값이 LCS의 길이이므로 출력
print(max(cache)) 