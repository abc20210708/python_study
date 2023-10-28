## FBI (브론즈 3)

tmp = []

for i in range(1, 6):
    s = input().rstrip()
    if 'FBI' in s:
        tmp.append(str(i))

if tmp:
    print(' '.join(tmp))
else:
    print("HE GOT AWAY!")