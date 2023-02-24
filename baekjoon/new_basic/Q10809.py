# 알파벳 찾기

## 참고 블로그 https://ooyoung.tistory.com/68
word = "baekjoon"
alph = list(range(97, 123))

for i in alph:
    print(word.find(chr(i)), end=" ")
