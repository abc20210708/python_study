# 럭키 스트레이트

'''
캐릭터 점수를 N이라할때 자릿수를 기준으로 점수 N을 반으로 나누어
왼쪽 자릿수 합과 오른쪽 부분의 자릿수 합이 더한 값이 동일한 상황

'''

n = "7755"
# 길이는 6

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
