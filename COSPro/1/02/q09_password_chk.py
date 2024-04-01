## 문제9) 비밀번호 검사

def solution(psw):
    length = len(psw)
    
    for i in range(length - 2):
        first_chk = ord(psw[i+1]) - ord(psw[i])
        second_chk = ord(psw[i]) - ord(psw[i-1])
        if first_chk == second_chk and (first_chk == 1 or first_chk == -1):
            return False
    return True
    
    
password1 = "cospro890"
ret1 = solution(password1)

print("solution 함수의 반환 값은", ret1, "입니다.")

password2 = "cba323"
ret2 = solution(password2)

print("solution 함수의 반환 값은", ret2, "입니다.")