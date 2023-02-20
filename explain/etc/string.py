## 참고 블로그 https://covenant.tistory.com/142

# 3-1 문자열을 거꾸로
alph = "ABCD"
print(alph[::-1])

inputStr = input()
if inputStr == inputStr[::-1]:
    print(1)
else:
    print(0)
    
# 3-2 문자열 <-> 아스키코드
ord() # 문자를 아스키코드로 변환하는 함수
chr() # 아스키코드를 문자로 변환하는 함수
