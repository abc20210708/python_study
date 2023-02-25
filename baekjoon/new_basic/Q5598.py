# 카이사르 암호

target = input()

     
x = input()
y = ''
for i in x :
    if i in "ABC":
        y += chr(ord(i) + 23)
    else:
        y += chr(ord(i) - 3)
        
print(y)

'''
for i in target:
    if ord(i) >= 65 and ord(i) <= 67:
        print(chr(ord(i)+23), end="")
    else:
        print(chr(ord(i)-3), end="")
'''