
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
