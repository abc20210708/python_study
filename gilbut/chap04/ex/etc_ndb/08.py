## 문자열 재정렬

'''
알파벳 대문자와 숫자로만 구성된 
문자열이 입력으로 주어집니다.

이때 모든 알파벳을 오른차순으로 
정렬하여 이어서 출력한 뒤에,
그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

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