
'''
문자열을 입력받아 해당 문자열의 회문 여부를 
판별하는 함수를 구현하세요. 
(회문: 앞으로 읽으나 뒤로 읽으나 같은 단어)

예시 입력: "level"
예시 출력: True
'''

s = "level"

def isTrue(s):
    temp = s[::-1]
    if s == temp:
        return True
    return False

print(isTrue(s))


def is_palindrome(s):
    s = s.lower() # 대소문자 구분 없이 판단위해 변환
    reversed_s = s[::-1] # 문자열을 뒤집은 문자열 생성
    
    #두 문자열이 같은지 비교하여 True 또는 False
    return s == reversed_s

print(is_palindrome(s))