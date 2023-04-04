## 미아 노트 (실버 5) *

# 참고 블로그 https://jeonnew.tistory.com/4

n, h, w = map(int, input().split())
l = [[] for _ in range(h)]
for i in range(h):
    inp = input()
    for j in inp:
        l[i].append(j)
result = ""   
jj = 0
while True:
    if len(result) == n:
        break
        
    word = '?'
    for i in range(h):
        for j in range(jj,jj+w):
            if l[i][j] != '?':
                word = l[i][j]
                break
                
    result += word
    jj += w
                
print(result)



# 참고 블로그 https://dreamtreeits.tistory.com/147
import sys

n, h, w = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(h)]

def solution(x):
    global res
    for i in range(x * w, (x + 1) * w):
        for j in range(h):
            if arr[j][i] != "?":
                res += arr[j][i]
                return
    res += "?"
    return


res = ""
for i in range(n):
    solution(i)
print(res)


# 참고 블로그 https://kimbj061116.tistory.com/2

def note(i):                # 문자열 만드는 함수
    global ans
    for j in range(w * i,w * (i+1)): # 노트를 문자열의 길이만큼 나눔
        for k in range(h):      
            if s[k][j]!='?':     # 나눈 부분 중에서 '?'가 아닌 문자가 있으면 그 문자를 더함
                ans += s[k][j]
                return
    ans += '?'         # 모든 문자가 '?'이면 '?'를 더함
    return
            
n, h, w=map(int, input().split())
s = [list(input()) for _ in range(h)]
ans='' 
                      
for i in range(n):
    note(i)
print(ans)
