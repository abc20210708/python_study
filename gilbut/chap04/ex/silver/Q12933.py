## 오리 (실버 3) *

# 참고 블로그 https://yuna0125.tistory.com/179
quack = 'quack'
duck = "quqacukqauackck"
#duck = input()
visitied = [0] * len(duck)

def solution(start):
    global cnt
    j = 0
    first = 1
    for i in range(start, len(duck)):
        # 울음 소리 비교
        if duck[i] == quack[j] and not visitied[i]:
            visitied[i] = 1
            if duck[i] == 'k':
                if first:
                    cnt += 1
                    first = 0
                j = 0
            else:
                j += 1

if len(duck) % 5 != 0:
    print(-1)
    exit()
    
cnt = 0
for i in range(len(duck)):
    if duck[i] == 'q' and not visitied[i]:
        solution(i)
        
if cnt == 0 or not all(visitied):
    print(-1)
else:
    print(cnt)
                