## 사이클 단어 (실버 4)

## 다른 풀이
#  참고 블로그 https://hueco.tistory.com/259

from collections import deque

n = int(input())
chk = set()
chk.add(input())
for _ in range(n-1):
    word = deque(input())
    for _ in range(len(word)):
        tmp = ''.join(word)
        if tmp in chk:
            break
        word.rotate()
    else:
        chk.add(''.join(word))
print(len(chk))






#  참고 블로그 https://velog.io/@xenrose/Python-%EB%B0%B1%EC%A4%80-1544%EB%B2%88-%EC%82%AC%EC%9D%B4%ED%81%B4-%EB%8B%A8%EC%96%B4

from collections import deque

def rotate_word(w1, w2):
    if len(w1)!=len(w2): return w2
    w2 = deque(w2)
    
    for _ in range(len(w2)):
        w2.rotate(1)
        t = ''.join(w2)
        if w1==t: return t
    
    return ''.join(w2)


n = int(input())
l = [input() for _ in range(n)]

for i in range(n):
    for j in range(i,n):
        if l[i]!=l[j]:
            l[j] = rotate_word(l[i], l[j])

print(len(set(l)))

