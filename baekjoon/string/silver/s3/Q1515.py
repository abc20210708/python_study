# 수 이어 쓰기 (실버 3) *

## 참고블로그 https://latte-is-horse.tistory.com/373
'''
예제 234092로 예를 들면

234092 -> n = [2,3,4,0,9,2]

cnt = 1 일때 n 배열에 포함되는 것이 
없으므로 cnt += 1

cnt = 2 일때 n[0] = 2이므로 n의 1번째 항을 
지워주고 n을 다시 정의한다 -> n =[3,4,0,9,2]

cnt = 3 일때 n[0] = 3이므로 n의 1번째 항을 지워주고
-> n =[4,0,9,2]

cnt = 4 일때 n[0] = 4이므로n의 1번째 항을 지워주고
-> n =[0,9,2]

 

cnt = 10일때 result[0] = 1과 n[0] = 0은 일치하지 않으므로
result의 1번째 항을 지워주고 
result[1,0] -> result[0]

result[0] = 0 n[0] = 0 서로 일치하므로 n의 1번째 항을 
지워주고 -> n[9,2]

 

cnt = 19 일때 result[0] = 1과 n[0] = 9은 일치하지 않으므로 
result의 1번째 항을 지워주고
result[1,9] -> result[9]

result[0] = 9 n[0] = 9 서로 일치하므로 
n의 1번째 항을 지워주고 -> n[2]

 

cnt = 20 일떄 result[0] = 2과 n[0] = 2은 일치하므로 
n의 1번째 항을 지워주고  -> n[]

지워진 숫자를 모두 찾았으므로 결과를 출력한다
'''
# 234092
'''
nums = input()
i = 0
while 1:
    i += 1
    num = str(i)
    while len(num) > 0 and len(nums) > 0:
        if num[0] == nums[0]:
            nums = nums[1:]
        num = num[1:]
    if nums == '':
        print(i)
        break
'''  
## 참고 블로그 http://oripre.tistory.com/67
import sys
n = sys.stdin.readline().rstrip()
# n의 최솟값을 저장할 변수를 0으로 초기화
cnt = 0 
while len(n) > 0: # 남은 수가 비어있지 않을 때까지 반복
    # n의 후보 값, cnt를 1씩 증가
    cnt += 1
    # cnt를 문자열로 변환하여 result에 저장
    result = str(cnt)
    # result와 n이 둘 다 비어있지 않을 때까지 반복
    while result and n:       
        # result와 n의 첫 번재 숫자를 비교해 같으면
        #print(n[0])
        if result[0] == n[0]:
            # n의 첫 번째 숫자를 제거
            n = n[1:]
        # result의 첫 번째 문자를 제거
        result = result[1:]
print(cnt)