'''
주어진 문자열에서 각 단어의 첫 글자를 
대문자로 바꾸고, 나머지 글자는 
모두 소문자로 바꾼 결과를 출력하는 함수를 구현하세요.

예시 입력: "ThIs iS a TeSt"
예시 출력: "This Is A Test"

'''
s = "ThIs iS a TeSt"

temp = s.split()
print(temp)

for i in temp:
    i = i[:1].upper() + i[1:].lower()
    print(i, end=" ")