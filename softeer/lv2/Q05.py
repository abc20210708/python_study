# 비밀 메뉴

# 참고 블로그 https://thflgg133.tistory.com/98
import sys

m, n, k = map(int, sys.stdin.readline().split())


# join 함수를 이용해 리스트로 받은 비밀 메뉴를 문자열화 시킴

s_menu = ''.join(list(sys.stdin.readline().rstrip().split()))

# join 함수를 이용해 리스트로 받은 button을 문자열화 시킴
button = ''.join(list(sys.stdin.readline().rstrip().split()))
print(f"s_menu: {s_menu}")
print(f"button: {button}")


if s_menu in button:
    print("secret")
else:
    print("normal")
    
'''
참고 블로그 https://blockdmask.tistory.com/468

''.join(리스트)

'구분자'.join(리스트)

join 함수는 매개변수로 들어온 리스트에 있는 
요소 하나하나를 합쳐서 하나의 문자열로 
바꾸어 반환하는 함수입니다.

- ''.join(리스트)
''.join(리스트)를 이용하면 매개변수로 
들어온 ['a', 'b', 'c'] 이런 식의 리스트를 
'abc'의 문자열로 합쳐서 반환해주는 함수인 것입니다.

- '구분자'.join(리스트)
'구분자'.join(리스트)를 이용하면 리스트의 
값과 값 사이에 '구분자'에 들어온 구분자를 
넣어서 하나의 문자열로 합쳐줍니다.
'_'.join(['a', 'b', 'c']) 라 하면 
"a_b_c" 와 같은 형태로 문자열을 만들어서 반환해 줍니다.

예. 눈치 빠르신 분들은 눈치채셨겠지만
처음에 소개 해준 ''.join(리스트)는 
'구분자'.join(리스트)에서 '구분자'가 그냥 공백인 것과 같습니다.

즉, 정리하자면 join함수의 찐 모양은 '구분자'.join(리스트) 입니다.
'''