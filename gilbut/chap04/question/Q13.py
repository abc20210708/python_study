# 신규 아이디 추천
import re
'''
아이디 길이는 3자 이상 15자 이하
아이디는 알파벳 소문자, 숫자, -_. 만 사용
(.) 마침표는 처음과 끝에 사용할 수 없고 연속 사용 불가
'''
def solution(temp):

    # 1. 모든 대문자를 소문자로
    temp = temp.lower()

    # 2. 알파벳 소문자, 숫자, -_. 제외한 모든 문자 제거
    temp = re.sub(r"[^a-z0-9-_.]", "", temp)

    # 3. 마침표가 2번 이상이면 연속된 부분을 하나로 치환
    while ".." in temp:
        if ".." in temp:
            temp = temp.replace("..", ".")

    # 4. 마침표가 처음이나 끝에 위치하면 제거
    if temp[0] == '.':
        temp = temp[1:]
    elif temp[-1] == '.':
        temp = temp[:-1]
        
    # 5. 빈 문자열이라면 temp에 "a"를 대입
    if temp == '':
        temp = "a"
        
    # 6. temp 길이가 16자 이상이면
    # 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    if len(temp) >= 16:
        temp = temp[:15]

    # 6-1. 제거 후 마침표(.)가 끝에 위치한다면
    # 끝에 위치한 마침표(.) 문자를 제거
    if temp[-1] == '.':
        temp = temp[:-1]
        
    # 7. temp 길이가 2자 이하라면
    # tmep 마지막 문자를 temp의 길이가 3이 될 때까지 끝에 붙임
    if len(temp) <= 2:
        target = temp[-1]
        while len(temp) != 3:
            temp += target
        
    print(solution("...!@BaT#*..y.abcdefghijklm"))
    
    return temp

        