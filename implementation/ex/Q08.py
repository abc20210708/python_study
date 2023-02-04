
# 문자의 재정렬

s = "K1KA5CB7"

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