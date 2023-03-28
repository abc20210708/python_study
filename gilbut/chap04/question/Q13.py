# 신규 아이디 추천


def explain(temp):
    # 1. 문자열 전체를 소문자로 변환
    res = temp.lower()
    
    # 2. 지정된 문자를 제외한 나머지 문자를 전부 제거
    filtered = []
    for c in res:
        if c.isalpha() or c.isdigit() or c in ('-', '_', '.'):
            filtered.append(c)
    res = ''.join(filtered)
    
    # 3.마침표가 2번 찍혔다면 그 중 하나만 제거
    while '..' in res:
        # replace는 가장 먼저 발견된 것만 수정
        res = res.replace("..", ".")
    
    # 4. 마침표 양옆으로 문자열을 1개씩 제거
    res = res.strip('.')
    
    # 5. 전부 제거했는데, 아무것도 없다면 'a'를 할당
    if res == '' : res = "a"
    
    # 6. 나온 결과가 16자 이상이면 그 이상은 모두 삭제,
    # 마지막 문자가 따옴표인 경우 따옴표 삭제
    if len(res) > 15 : res = res[:15]
    if res[-1] == '.': res = res[:-1]
    
    # 7. 반대로 3자 미만이면 마지막 문자를 반복해서 3글자 이상으로
    while len(res) < 3:
        res += res[-1]
        
    return res


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

    '''
    2. 문자열에서 숫자만 남기기
    숫자를 제외한 문자들을 패턴으로 만들면 [^0-9]가 됩니다. 
    0-9는 0에서 9사이의 숫자를 의미하고 ^는 not이므로, 
    숫자가 아닌 문자열을 찾는 패턴이 됩니다.

    import re

    string = "AA**BB#@$CC 가나다-123"

    new_str = re.sub(r"[^0-9]", "", string)
    print(new_str)
    
    Output:
    123
    
    참고 블로그 https://codechacha.com/ko/python-remove-special-letters/
    '''

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

        