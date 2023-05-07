# 배 (골드 5) 

# 참고 코드 https://www.acmicpc.net/source/52479122
# 크레인의 수 입력
n = int(input())   
# 각 크레인의 무게 입력             
cranes = list(map(int, input().split()))  
# 화물 상자의 수 입력
m = int(input())   
# 각 화물 상자의 무게 입력             
boxes = list(map(int, input().split()))   
# 옮긴 횟수를 나타내는 변수 초기화
cnt = 0                         
# 크레인의 무게를 내림차순으로 정렬
cranes.sort(reverse=True)  
# 화물 상자의 무게를 내림차순으로 정렬     
boxes.sort(reverse=True)        

# 크레인이 들 수 있는 화물 상자만을 남김
cranes = [crane for crane in cranes if crane >= boxes[m-1]]  

# 크레인이 가장 무거운 화물보다 작거나, 크레인이 없는 경우
if not cranes or cranes[0] < boxes[0]:   
    print(-1) # 모든 화물을 옮길 수 없으므로 -1 출력
else:                           
    while boxes: # 아직 옮겨야 할 화물 상자가 남아있는 동안 반복
        for crane in cranes: # 각 크레인에 대해서
            for box in boxes:  # 각 화물 상자에 대해서
                if crane >= box:  # 크레인이 화물 상자를 들 수 있다면
                    boxes.remove(box)# 해당 화물 상자를 옮김
                    break # 다음 크레인으로 넘어감
        cnt += 1# 옮김 횟수 증가
    print(cnt) 






# 참고 블로그 https://velog.io/@ju_h2/Python-%EB%B0%B1%EC%A4%80-1092.-%EB%B0%B0-%ED%92%80%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%83%90%EC%9A%95-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EA%B7%B8%EB%A6%AC%EB%94%94-%EA%B5%AC%ED%98%84-5
n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

# 내림차순 정렬
crane.sort(reverse = True)
box.sort(reverse = True)

time = 0 # 시간
checked = [0 for _ in range(m)] # 박스를 옮겼는지 여부
cnt = 0 # 옮긴 박스의 개수 

p = [0] * n

if max(box) > max(crane):
    print(-1)
else:
    while cnt < len(box):
        for i in range(n): # 크레인에 대하여
            while p[i] < len(box):
            # 아직 안 옮긴 박스 중에서, 
            # 옮길 수 있는 박스를 만날 때까지 반복
                if not checked[p[i]] and crane[i] >= box[p[i]]:
                    checked[p[i]] = True
                    p[i] += 1
                    cnt += 1
                    break
                p[i] += 1
        time += 1
    print(time)    