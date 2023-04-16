## 오리 (실버 3) *

# 참고 블로그 https://yuna0125.tistory.com/179
quack = 'quack'
str = "quqacukqauackck"
#str = "kcauq"
#duck = input()
visitied = [0] * len(str)

def solution(start):
    global cnt
    j = 0
    first = 1
    for i in range(start, len(str)):
        # 울음 소리 비교
        if str[i] == quack[j] and not visitied[i]:
            visitied[i] = 1
            if str[i] == 'k':
                if first:
                    cnt += 1
                    first = 0
                j = 0
            else:
                j += 1

if len(str) % 5 != 0:
    print(-1)
    exit()
    
cnt = 0
for i in range(len(str)):
    if str[i] == 'q' and not visitied[i]:
        solution(i)
        
if cnt == 0 or not all(visitied):
    print(-1)
else:
    print(cnt)
                
'''
"quqacukqauackck"와 같은 문자열을 보면, 
이 문자열은 "quack"이라는 소리를 여러 번 반복하면서, 
중간에 잡음이 섞인 형태로 구성되어 있습니다.

하지만 이 문자열에서는 "quack"이 몇 번 반복되었는지 알 수 없습니다. 
즉, 이 문자열이 한 마리 오리가 울었는지, 
두 마리 이상의 오리가 울었는지는 알 수 없습니다.

따라서 이 문자열이 두 마리 이상의 오리가 울었다고 보기 위해서는, 
"quack"이라는 단어의 각 글자가 연속해서 나타나는 순서를 고려해야 합니다. 

예를 들어, "quackquack"이라는 문자열은 "quack"이 두 번 연속해서 나타나므로, 
두 마리의 오리가 울었다고 볼 수 있습니다.

하지만 "quqacukqauackck"와 같이 "quack"의 글자들이 섞여 나타나는 경우, 
이 문자열이 몇 마리의 오리가 울었는지 알기 위해서는 
"q"가 "u"보다 먼저 나타나야 하고, "u"가 "a"보다 먼저 나타나야 하며, 
"a"가 "c"보다 먼저 나타나야 합니다. 

이렇게 순서가 일치하도록 "quack"이라는 단어를 찾으면, 
그것이 한 마리의 오리가 울은 것이라고 가정할 수 있습니다.

따라서 "quqacukqauackck"와 같은 문자열은 "quack"의 순서가 일치하지 않으므로, 
이 문자열은 한 마리 이상의 오리가 울은 것으로 가정할 수 있습니다.
'''