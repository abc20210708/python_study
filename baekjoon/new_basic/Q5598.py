# 카이사르 암호

target = input()

for i in target:
    if ord(i) >= 65 and ord(i) <= 67:
        print(chr(ord(i)+23), end="")
    else:
        print(chr(ord(i)-3), end="")
        
