## 마니또 (실버 1)

## 참고 코드 https://www.acmicpc.net/source/47207355
import sys

input = sys.stdin.readline
caseNum = 0

while True:
    
    n = int(input())
    if n == 0:
        break
    caseNum += 1
    manito = dict()
    
    for _ in range(n):
        toYou, toMe = map(str, input().split())
        manito[toYou] = toMe
        
    cnt = 0
    
    while manito:
        origin = next(iter(manito)) ##ChatGPT 참고 
        start = origin
        end = manito.get(start)
        manito.pop(start)
        
        while end in manito.keys():
            start = end
            end = manito.get(start)
            if end == origin:
                cnt += 1
            manito.pop(start)
    print(caseNum, cnt)

## ChatGPT 참고 - origin = next(iter(manito)) 

'''

next(iter(manito))은 Python 코드에서 사용되는 여러 개의 
데이터를 저장할 수 있는 자료구조인 딕셔너리(dict) manito에서 
첫 번째 키-값 쌍을 가져오는 부분입니다.


1. manito는 딕셔너리 자료형입니다. 딕셔너리는 키(key)와 
값(value)을 연관시키는 데이터 구조로, 특정 키를 사용하여 
해당 키와 연관된 값을 빠르게 찾을 수 있습니다.

2. iter(manito)는 manito 딕셔너리의 이터레이터(iterator)를 
생성합니다. 이터레이터는 반복문에서 데이터를 하나씩 순회하며 
가져오는 역할을 합니다.

3. next(iter(manito))는 이터레이터에서 다음 값을 가져오는 
함수입니다. 딕셔너리의 경우, 이 함수를 사용하면 딕셔너리의 
키(key) 중에서 첫 번째 키를 가져옵니다. 이때, 딕셔너리의 순서는 
키가 추가된 순서가 아니라 임의로 정해집니다. 
Python 3.7 이전 버전에서는 딕셔너리의 순서가 보장되지 않았지만, 
Python 3.7부터는 키-값 쌍이 입력된 순서대로 유지됩니다.

따라서 next(iter(manito))는 manito 딕셔너리에서 첫 번째 키를 
가져올 것이며, 이 키는 변수 origin에 저장됩니다. 
이 코드는 딕셔너리에서 첫 번째 키를 가져와서 해당 키에 
연관된 값을 찾을 때 사용됩니다. 이후에는 해당 키와 연관된 값을 
사용하고 나면, 해당 키-값 쌍을 딕셔너리에서 제거하게 됩니다.

'''

## 유니온 파인드 참고한 풀이 추가
#  분리 집합 https://www.jongung.com/292
#  참고 블로그 https://blog.naver.com/ej_0109/222801473404
def find(x) :
    if x != parent[x] :
        parent[x] = find(parent[x])
    return x

def union(x,y) :
    x = find(x)
    y = find(y)

    if x < y :
        parent[y] = x
    else :
        parent[x] = y

cnt = 0
while True :
    n = int(input())
    parent = [i for i in range(n + 1)]
    m = {}
    cnt += 1

    if n == 0 :
        break

    for _ in range(n) :
        t1, t2 = map(str, input().split())

        if not t1 in m :
            m[t1] = len(m) + 1
        if not t2 in m :
            m[t2] = len(m) + 1

        union(parent[m[t1]], parent[m[t2]])

    parent = set(parent)
    print(cnt, len(parent)-1)






#  참고 블로그 https://velog.io/@jsbryan/BOJ%EB%B0%B1%EC%A4%805107-Silver-1-%EB%A7%88%EB%8B%88%EB%98%90-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC


input= sys.stdin.readline

def dfs(v): #dfs
    global check
    visited[v]= True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            visited[i] = True
            check += 1

case = 1 #케이스 번호

while True:
    N = int(input())
    cnt = 1 # 마니또 이름을 숫자로 바꿔서 저장할 변수
    li= dict() #사람들의 이름을 정수로 바꿔서 저장할 딕셔너리
    if N == 0: 
        break
    graph = [ [] for _ in range(N+1)]
    manitto = []
    answer = 0
    for _ in range(N):
        a, b= map(str,input().split())
        manitto.append([a,b])
        if a not in li.keys(): # { 'Andrew' :0, "Sally' : 1 } 과 같은 형식으로 저장
            li[a]= cnt
            cnt +=  1
        if b not in li.keys(): # 마찬가지
            li[b] = cnt
            cnt += 1

    for a,b in manitto: # 이름들의 value값을 받아와서 그래프로 변환한다. 
        k= li.get(a)
        t= li.get(b)
        graph[k].append(t)

    result = []
    for i in range(1,N+1): #마니또를 찾을차례
        if i in result: #만약 해당 사람이 마니또 연결고리에 이미 들어가있으면 중복 제외처리한다. 
            continue
        check = 1
        visited= [False] *(N+1) 
        dfs(i) # i번째 사람부터 dfs를 돌기 시작한다. 
        if check == visited.count(True): #dfs 돌고 마니또 연결고리를 찾으면
            for i in range(len(visited)):
                if visited[i]== True:
                    if i not in result: #해당 사람들을 result에 추가해서 중복을 제외할 수 있도록한다.
                        result.append(i)
            answer +=1 #연결고리 하나를 추가한다.
    
    print("{} {}".format(case,answer))

    case += 1