## 문제4) 중복 문자열 이어 붙이기
#  참고 블로그 https://velog.io/@corone_hi/COS-PRO-1%EA%B8%89-3%EC%B0%A8-%EB%AC%B8%EC%A0%9C4-%EC%A4%91%EB%B3%B5-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%9D%B4%EC%96%B4%EB%B6%99%EC%9D%B4%EA%B8%B0

def solution(s1, s2):
    answer = 0
    tmp = min(len(s1), len(s2))
    
    for i in range(tmp):
        if s1[:i] == s2[-i:] or s2[:i] == s1[-i:]:
            #print("s1[:i]", s1[:i])
            #print("s2[-i:]", s2[-i:])
            #print("s2[:i]", s2[:i])
            #print("s1[-i:]", s1[-i:])
            answer = i
    
    return len(s1) + len(s2) - answer



s1 = "ababc"
s2 = "abcdab"
ret = solution(s1, s2)

print("solution 함수의 반환 값은", ret, "입니다.")