## 여우는 어떻게 울지? (실버 4) *

# 참고 블로그 https://fre2-dom.tistory.com/353
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    sound = list(map(str, input().split()))
    
    while 1:
        animal = list(map(str, input().split()))
        
        if animal[0] == "what":
            print(" ".join(sound))
            break
        
        while animal[2] in sound:
            sound.remove(animal[2])


