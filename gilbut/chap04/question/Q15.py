## 핸드폰 번호 가리기

def solution(phone_number):
    res = '*' * (len(phone_number) - 4)
    res += phone_number[-4:]
    
    return res