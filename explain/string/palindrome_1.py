'''
슬라이싱

s = ["가나다다나가"]

if s == s[::-1]:
    print("회문이다")
    

'''

## 참고 블로그 https://han-py.tistory.com/331
import re

def inPalindrome(str):
    # 소문자로 변경
    str = str.lower()
    
    # 정규식 사용
    str = re.sub('[^a-z0-9]', '', str)
    if str == str[::-1]:
        print("회문입니다")
    else:
        print("회문이 아닙니다")
        
a = '0Madam, I\'m Adam0'
inPalindrome(a)
    
'''
re.sub('패턴', '바꿀문자열', '적용할문자열')
ex_

  print( re.sub('[0-9]+', 'n', '1 2 Fizz 4 Buzz Fizz 7 8') ) # 숫자만 찾아서 n으로 바꿈

 
  'n n Fizz n Buzz Fizz n n'
'''