## 암호 (브론즈 2) *

text, key = input(), input()

res = ''

for i in range(len(text)):
    if text[i] == " " : res += " "
    else: res += chr((ord(text[i]) - ord(key[i%len(key)])-1) % 26 + ord('a'))
print(res)

# 대응하는 암호와 키의 문자의 코드를 더해 계산
# 범위가 벗어날 수 있으므로 알파벳 개수인 26을 나눠줌
# 참고 블로그 https://neomindstd.github.io/%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4/boj1718/