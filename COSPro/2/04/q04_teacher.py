## 문제4) 조교의 수 구하기. - Python3

def solution(classes, m):
    answer = 0
    
    for students in classes:
        answer += students // m
        if students % m != 0:
            answer += 1
    return answer

classes = [80, 45, 33, 20]
m = 30
res = solution(classes, m)

print("solution 함수의 반환 값은", res, "입니다.")
