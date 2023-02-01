# 모험가 길드

n = int(input())

data = list(map(int, input().split()))                
data.sort()

result = 0 # 총 그룹의 수
cnt = 0 # 현재 그룹에 포함된 모험가의 수

for i in data : # 공포도가 낮은 것부터 하나씩 확인
    cnt += 1 # 현재 그룹에 해당 모험가를 포함
    if cnt >= i : # 현재 그룹에 포함된 모험가의 수가 
                 #현재의 공포도 이상이라면, 그룹 결성
        result += 1
        cnt = 0


print(result)
        

'''
잎에서부터 공포도를 하나씩 확인하며,
'현재 그룹에 포함된 모험가의 수'가
'현재 확인하고 있는 공포도' 보다 크거나 같다면
그룹으로 설정
'''
