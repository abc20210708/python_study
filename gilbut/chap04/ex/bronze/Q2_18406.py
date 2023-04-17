## 럭키 스트레이트 (브론즈 2)

s = input()
cnt = 0

for i in range(len(s)):
    if i < (len(s) // 2):
        cnt += int(s[i])
    else:
        cnt -= int(s[i])

if cnt == 0:
    print("LUCKY")
else:
    print("READY")