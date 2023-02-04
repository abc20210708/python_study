# 럭키 스트레이트

'''
캐릭터 점수를 N이라할때 자릿수를 기준으로 점수 N을 반으로 나누어
왼쪽 자릿수 합과 오른쪽 부분의 자릿수 합이 더한 값이 동일한 상황

'''

n = "123402"

length = len(n)
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(length // 2) :
    summary += int(n[i])

for i in range(length // 2, length) :
    summary -= int(n[i])
    
    
# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검색
if summary == 0:
    print("LUCKY")
else:
    print("READY")    


'''
num1, num2 = 0 , 0
for i in range(len(n)) :
    if i >= len(n) / 2 :
        num2 += int(n[i])
    else :
        num1 += int(n[i])
    
if num1 == num2 :
    print("LUCKY")
else :
    print("READY")
'''