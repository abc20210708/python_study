## 문제9) 분침과 시침의 각도 구하기

def solution(hour, minute):
    h = (360/12) * hour + (360/12/60) * minute
    m = (360/60) * minute
    
    answer = abs(h-m) 
    if answer > 180:
        answer = 360 - answer
        
    return "{:.1f}".format(answer)

hour = 3
minute = 0
ret = solution(hour, minute)

print("solution 함수의 반환 값은", ret, "입니다.")