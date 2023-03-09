# 회문

'''
팰린드롬이란 앞뒤가 똑같은 단어나 문장을 의미한다.
이때, 대소문자를 구분하지 않으며 글자와 숫자만 따지면 된다.
    ex ) '가나다다나가'
'''

def isPalidrome(str):
    for i in range(len(str) // 2):
        #print(-i-1)
        if str[i] == str[-i-1]:
            continue
        else:
            print("회문이 아닙니다.")
            return
    print("회문입니다.")
    
data = "abcba"
isPalidrome(data)
    