
# 곱하기 혹은 더하기 다시 풀기

'''
0~9로만 이루어진 문자열 S가 주어졌을 때,
왼쪽으로부터 오른쪽으로 하나씩 모든 숫자를 확인하며
숫자 사이에 x 혹인 + 연산 넣어서 가장 큰 수
'''

s = "567"

# 0이나 1일 때는 더하고 / 나머지는 곱하기

num = int(s[0])

for i in range(1, len(s)):
    if num == 0 or int(s[i]) < 2 :
        num += int(s[i])
    else:
        num *= int(s[i])
        
print(num)
        

    


