## 민균이의 비밀번호 (브론즈 1) *

'''
파일의 목록에 원래의 비밀번호,
비밀번호를 역순으로 한 단어가 있다.
'''

n = int(input())
words = [input() for _ in range(n)]

for word in words:
    if word[::-1] in words:
        print(len(word), word[len(word) // 2])
        break