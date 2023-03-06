# ROT13 

#import sys
#target = sys.stdin.readline()
target = "One is 1"
temp = ""

for i in target:
    if 'a' <= i <= 'z':
        temp += chr((ord(i) + 13) if i <= 'm' else ord(i) - 13)
    elif 'A' <= i <= 'Z':
        temp += chr((ord(i) + 13) if i <= 'M' else ord(i) - 13)
    else:
        temp += i
        
print(temp)
        


'''
for i in target:
    if i == " ":
        print(" ", end="")
    elif i.islower():
        temp = ord(i) + 13
        if temp > 122:
            temp -= 26
        print(chr(temp), end="")
    elif i.isupper():
        temp = ord(i) + 13
        if temp > 90:
            temp -= 26
        print(chr(temp), end="")
    elif ord(i) >= 48 and 57 >= ord(i):
        print(i, end="")
'''