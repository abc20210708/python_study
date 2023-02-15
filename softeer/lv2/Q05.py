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