## 진짜 메시지 (실버 5)
#  참고 코드 https://www.acmicpc.net/source/64801600
import sys

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    
    alp = [0] * 26
    tmp = input()
    chk = True

    for i in range(len(tmp) -1):
        num = ord(tmp[i]) - ord('A')
        alp[num] += 1

        if alp[num] == 3 :
            if tmp[i] != tmp[i+1] :
                chk = False
                break
            else:
                alp[num] = -1

    
    if chk:
        print('OK')
    else :
        print('FAKE')        


