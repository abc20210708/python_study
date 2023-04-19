## 오리 (실버 3) *

# 참고 블로그 https://yuna0125.tistory.com/179
# "quack"이라는 문자열이 주어진 문자열에서 
# 몇 번 나타나는지 세는 문제를 해결하는 코드

# 찾아야 할 문자열 "quack"을 변수에 저장
quack = 'quack'                  
str = input()  
# 문자열의 길이만큼의 리스트를 생성하고 
# 0으로 초기화된 방문 여부 리스트 생성       
visited = [0] * len(str)         

def solution(start):
    # 전역 변수 cnt를 사용하기 위해 선언
    global cnt 
    # "quack" 문자열의 인덱스를 나타내는 변수             
    j = 0
    # 첫 번째 'k'인 경우를 체크하기 위한 변수   
    first = 1                     
    for i in range(start, len(str)):
        # 현재 문자와 "quack"의 문자를 비교하고 방문하지 않은 경우에만 실행
        if str[i] == quack[j] and not visited[i]:    
            visited[i] = 1  # 현재 문자를 방문 처리
            if str[i] == 'k':  # 현재 문자가 'k'인 경우
                if first:   # 첫 번째 'k'인 경우
                    cnt += 1  # 카운트를 증가
                    first = 0  # 첫 번째 'k'인 경우를 처리했음을 표시
                # 다음에 비교할 문자열의 인덱스를 초기화
                j = 0               
            else:
                # 다음에 비교할 문자열의 인덱스를 증가
                j += 1              

# 입력 문자열의 길이가 5의 배수가 아닌 경우
if len(str) % 5 != 0: 
    print(-1) # -1을 출력하고 프로그램 종료
    exit()

# "quack" 문자열이 몇 번 나타났는지 
# 카운트하는 변수 초기화
cnt = 0                          
for i in range(len(str)):  # 문자열의 각 문자에 대해 반복
    # 현재 문자가 'q'이고 방문하지 않은 경우
    if str[i] == 'q' and not visited[i]:   
        # solution 함수를 호출하여 "quack"이 나타나는지 확인
        solution(i)               

# "quack" 문자열이 하나도 나타나지 않거나 모든 문자가 방문되지 않은 경우
if cnt == 0 or not all(visited):   
    print(-1)  # -1을 출력
else: # 그렇지 않은 경우에는 "quack" 문자열이 나타난 횟수를 출력
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


duck = input()                 
visited = [False] * len(duck) 
# "quack" 문자열이 몇 번 나타났는지 
# 카운트하는 변수 초기화
cnt = 0                        

 # 입력 문자열의 길이가 5의 배수가 아닌 경우
 # -1을 출력하고 프로그램 종료
if len(duck) % 5 != 0:
    print(-1)                  
    exit()

def solve(start):
    # 전역 변수 cnt를 사용하기 위해 선언
    global cnt       
    # 찾아야 할 문자열 "quack"을 변수에 저장          
    quack = 'quack'      
    # "quack" 문자열의 인덱스를 나타내는 변수  
    # 첫 번째 'k'인 경우를 체크하기 위한 변수    
    j = 0                     
    first = True       
    for i in range(start, len(duck)):
        # 현재 문자와 "quack"의 문자를 비교하고 방문하지 않은 경우에만 실행
        if duck[i] == quack[j] and not visited[i]:   
            visited[i] = True   # 현재 문자를 방문 처리
            if duck[i] == 'k':  # 현재 문자가 'k'인 경우
                if first:       # 첫 번째 'k'인 경우
                    cnt += 1     # 카운트를 증가
                    first = False # 첫 번째 'k'인 경우를 처리했음을 표시
                j = 0             # 다음에 비교할 문자열의 인덱스를 초기화
                # 'k'인 경우는 더 이상 비교할 필요가 없으므로 
                # continue로 다음 반복으로 넘어감
                continue     
            # 다음에 비교할 문자열의 인덱스를 증가   
            j += 1               

# 문자열의 각 문자에 대해 반복
for i in range(len(duck)):      
    # 현재 문자가 'q'이고 방문하지 않은 경우
    if duck[i] == 'q' and not visited[i]:   
        solve(i)# solve 함수를 호출하여 "quack"이 나타나는지 확인

 # "quack" 문자열이 하나도 나타나지 않거나 모든 문자가 방문되지 않은 경우
if not all(visited) or cnt == 0: 
    print(-1) # -1을 출력
else:
    print(cnt)  # 그렇지 않은 경우에는 "quack" 문자열이 나타난 횟수를 출력