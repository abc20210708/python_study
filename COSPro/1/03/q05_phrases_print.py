## 문제5) 전광판 문구 출력

def solution(phrases, second):
    tmp = second % 14
    length = 14 - tmp
    answer = '_' * length
    
    for i in range(tmp):
        answer += phrases[i]
        
    return answer



phrases = "happy-birthday"
second = 3
ret = solution(phrases, second)

print("solution 함수의 반환 값은", ret, "입니다.")