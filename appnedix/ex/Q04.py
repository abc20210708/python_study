'''
주어진 문자열에서 각 단어의 첫 글자를 
대문자로 바꾸고, 나머지 글자는 
모두 소문자로 바꾼 결과를 출력하는 함수를 구현하세요.

예시 입력: "ThIs iS a TeSt"
예시 출력: "This Is A Test"

'''
s = "ThIs iS a TeSt"

temp = s.split()
# print(temp)

for i in temp:
    i = i[:1].upper() + i[1:].lower()
    print(i, end=" ")

'''
1. 문자열을 모두 소문자로 변환합니다.
2. 단어별로 문자열을 분리합니다.
3. 분리된 단어의 첫 글자를 대문자로 변환합니다.
4. 나머지 글자는 모두 소문자로 변환합니다.
5. 변환된 단어들을 다시 결합하여 최종 문자열을 반환합니다.

'''    

def solution(sentence):
    words = sentence.lower().split() # 1, 2
    capitalized_words = [word.capitalize() for word in words] # 3, 4
    return " ".join(capitalized_words)

print(solution(s))