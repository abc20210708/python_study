# 차량 번호판 다시 풀기


s = input()

forms = {'c':26, 'd':10}

res = forms[s[0]]
   
for i in range(1, len(s)):
    tmp = forms[s[i]]
    if s[i] == s[i - 1]:
        tmp -= 1
    res *= tmp
        
print(res)