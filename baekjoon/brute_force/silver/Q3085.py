## 사탕 게임 (실버 2)

import sys
input=sys.stdin.readline

def check(arr):
    n=len(arr)
    answer=1

    for i in range(n):
        # 열 순회하면서 연속되는 숫자 세기
        cnt=1
        for j in range(1, n):
            if arr[i][j] == arr[i][j-1]:
        	# 이전 것과 같다면 cnt에 1 더하기
                cnt += 1
            else:
            # 이전과 다르다면 다시 1로 초기화
                cnt=1
                
            # 비교해서 현재 cnt가 더 크다면 answer 갱신하기
            if cnt > answer:
                answer = cnt

        # 행 순회하면서 연속되는 숫자 세기
        cnt=1
        for j in range(1, n):
            if arr[j][i] == arr[j-1][i]:
        	# 이전 것과 같다면 cnt에 1 더하기
                cnt += 1
            else:
            # 이전과 다르다면 다시 1로 초기화
                cnt=1
                
            # 비교해서 현재 cnt가 더 크다면 answer 갱신하기
            if cnt > answer:
                answer = cnt

    return answer

n=int(input())
arr=[list(input()) for _ in range(n)]
answer=0

for i in range(n):
    for j in range(n):
        # 열 바꾸기
        if j+1 < n:
        	# 인점한 것과 바꾸기
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            
            # check는 arrd에서 인점한 것과 바꿨을 때 가장 긴 연속한 부분을 찾아내는 함수이다
            temp=check(arr)

            if temp > answer:
                answer = temp
               
            # 바꿨던 것을 다시 원래대로 돌려놓기
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

        # 행 바꾸기
        if i+1 < n:
        	# 인점한 것과 바꾸기
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            
            # check는 arrd에서 인점한 것과 바꿨을 때 가장 긴 연속한 부분을 찾아내는 함수이다
            temp=check(arr)

            if temp > answer:
                answer = temp
            
            # 바꿨던 것을 다시 원래대로 돌려놓기
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            
print(answer)


## 다른 풀이 
#  참고 블로그 https://ryngryng.tistory.com/37

n = int(input()) # 보드의 크기
candy = [list(input()) for _ in range(n)] # 사탕 색깔 정보

di = [1, 0] # 우하향 방향으로 탐색, 인접 사탕을 바꾸는 데 필요
dj = [0, 1]
answer=0

cnta, cntb = 1, 1 # 가로, 세로의 연속 사탕 개수 count
def check(graph, n):
    global cnta, cntb
    lst = [] # input 그래프의 모든 연속 정보를 저장하는 그래프
    for i in range(n):
        lst.append(cnta)
        lst.append(cntb)
        cnta, cntb = 1, 1
        for j in range(n-1): # j+1 까지가 탐색의 대상이므로 range < n-1
            
            if graph[i][j] == graph[i][j+1]: # 가로로 연속이라면
                cnta += 1 # cnta +1 처리
            else: # 연속이 끊어지면
                lst.append(cnta) # 저장하고
                cnta = 1 # 다시 세기 시작

            if graph[j][i] == graph[j+1][i]: # 세로로 연속이라면
                cntb += 1 # cntb +1 처리   
            else: # 연속이 끊어지면
                lst.append(cntb) # 저장하고
                cntb = 1 # 다시 세기 시작                       
    ans = max(lst)
    return(ans) # 저장된 모든 연속 정보의 최댓값 반환

for i in range(n):
    for j in range(n):
    
        for k in range(2): # graph[i][j] 점을 기준으로 우하향 이동
            if 0 <= i+di[k] < n and 0 <= j+dj[k] < n: # 보드의 크기 이내에서
                if candy[i][j] != candy[i+di[k]][j+dj[k]]: # 우측 or 아래 인접 사탕이 다르다면
                    candy[i][j], candy[i+di[k]][j+dj[k]] = candy[i+di[k]][j+dj[k]], candy[i][j]
                    tmp = check(candy, n) # 위치 변경하고 check
                    if tmp > answer:
                        answer = tmp # check한 값이 정답값보다 큰 경우 업데이트
                    # 다음 탐색을 위해 원상복귀    
                    candy[i][j], candy[i+di[k]][j+dj[k]] = candy[i+di[k]][j+dj[k]], candy[i][j]

print(answer)