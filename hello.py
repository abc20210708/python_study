# ROT13(11655) 다시 풀기

s = "Baekjoon Online Judge"
temp = ""

for i in s:
    if 'a' <= i <= 'z':
        temp += chr( ord(i)+13 if i <= 'm' else ord(i) - 13 )
    elif 'A' <= i <= 'Z':
        temp += chr( ord(i)+13 if i <= 'M' else ord(i) - 13 )
    else:
        temp += i
    
print(temp)


    
    
    


