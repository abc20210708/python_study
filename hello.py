# replace 매개변수 3개

text = "orange,orange,melon"
text_mod = text.replace("orange", "apple", 1)

temp = "apple,orange,melon"
print(text_mod)

'''
replace 메서드는 일치하는 검색 문자와 
일치하는 문자가 있는 경우 모두 변경합니다.

만약 제일 처음에 일치하는 문자만 치환하고 
싶은 경우에는 3번째 파라미터인 치환 횟수를 지정해주면 됩니다

가장 처음에 검색된 orange만 apple로 
치환되고 두 번째 orange는 치환되지 않았습니다.
'''