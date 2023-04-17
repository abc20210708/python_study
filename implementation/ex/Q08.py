
# 문자의 재정렬

s = "K1KA5CB7"
result = []
value = 0

# 문자를 하나씩 확인하며
for x in s:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else : value += int(x)
    
# 알파벳을 오름차순으로 설정
result.sort()

# t숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0 :
    result.append(str(value))
    
# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))



'''
list1 = list() #비어있는 리스트 만들기
result  = 0
for i in range(len(s)) :
    if ord(s[i]) >= 65 and ord(s[i]) <= 90:
        list1.append(s[i])
    else :
        result += int(s[i])
        
list1.sort()
st = ''.join(list1)

print(st + str(result))
'''

## 문자열 재정렬

'''
알파벳 대문자와 숫자로만 구성된 
문자열이 입력으로 주어집니다.

이때 모든 알파벳을 오른차순으로 
정렬하여 이어서 출력한 뒤에,
그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

'''

'''
s = "AJKDLSI412K4JSJ9D"
cnt = 0
res = []

for i in s:
    if ord(i) >= 65 and ord(i) <= 90:
        res.append(i)
    else:
        cnt += int(i)
        
res.sort()
print(''.join(res)+str(cnt))
'''