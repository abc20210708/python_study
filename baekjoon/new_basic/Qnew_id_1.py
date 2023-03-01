##참고 블로그 
## https://velog.io/@djagmlrhks3/Algorithm-Programmers-%EC%8B%A0%EA%B7%9C-%EC%95%84%EC%9D%B4%EB%94%94-%EC%B6%94%EC%B2%9C-by-Python
def solution(new_id):

    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    
    new_id = new_id.lower()


    # 2단계 new_id에서 
    # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를
    # 제외한 모든 문자를 제거합니다.
    ## isalnum()문자열이 영어, 한글 혹은 숫자로 되어있으면 참 리턴, 아니면 거짓 리턴.

    result = ''
    for word in new_id:
        if word.isalnum() or word in '-_.':
            result += word

    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을
    # 하나의 마침표(.)로 치환합니다.

    while '..' in result:
        result = result.replace("..", ".")


    # 4단계 new_id에서 마침표(.)가 
    # 처음이나 끝에 위치한다면 제거합니다.
    
    ## 삼항연산자 
    ## print("짝수") if a % 2 == 0 else print("홀수")
    ##[True] if [Condition] else [False]
    ##[참일때] if [조건문] else [거짓일때]
    

    result = result[1:] if result[0] == '.' and len(result) > 1 else result
    result = result[:-1] if result[-1] == '.' else result

    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.

    result = 'a' if result == '' else result



    # 6단계 new_id의 길이가 16자 이상이면, new_id의 
    # 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    # 만약 제거 후 마침표(.)가 new_id의 
    # 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.

    if len(result) >= 16:
        result = result[:15]
        
    if result[-1] == ".":
        result = result[:-1]

    # 7단계 new_id의 길이가 2자 이하라면, 
    # new_id의 마지막 문자를 new_id의 
    # 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

    if len(result) <= 3:
        result = result + result[-1] * (3-len(result))
        
    return result


print(solution("...!@88BaT#*..y.abcdefghijklm-._"))