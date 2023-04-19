## 핸드폰 번호 가리기
import re

def explain(phone_number):
    return re.sub('\d(?=\d{4})', '*', phone_number)
# \d는 해당하는 모든 숫자들을 검색하고, 
# 검색된 4글자를 제외해서 글자 길이에 상관없이
# 정확히 나머지를 *로 치환


def solution(phone_number):
    res = '*' * (len(phone_number) - 4)
    res += phone_number[-4:]
    print(phone_number[:-4]) #0103333
    print(phone_number[-4:]) #4444
    
    return res

print(solution("01033334444"))